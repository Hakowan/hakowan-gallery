#!/usr/bin/env python
"""Regenerate, validate, and index gallery recipes.

Examples run in isolated subprocesses so backend state, large meshes, and local
helper modules never leak between recipes.

Usage::

    pixi run -e full python render_gallery.py
    pixi run -e full python render_gallery.py Heat SPH
    pixi run -e full python render_gallery.py --check
    pixi run -e full python render_gallery.py --artifacts
    python render_gallery.py --check-artifacts
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import runpy
import subprocess
import sys
import time
import tempfile
import tomllib
from pathlib import Path
from typing import Any

GALLERY = Path(__file__).resolve().parent

# Every recipe is discovered from ``gallery/*/recipe.toml``; adding an example
# requires no handwritten registry update.

WEBP_QUALITY = 90
ARTIFACT_FORMAT_VERSION = "1"
_REQUIRED_MANIFEST_KEYS = {
    "id",
    "title",
    "script",
    "summary",
    "features",
    "backends",
    "inputs",
    "outputs",
}


def _manifests() -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for path in sorted(GALLERY.glob("*/recipe.toml")):
        manifest = tomllib.loads(path.read_text(encoding="utf-8"))
        _validate_manifest(path.parent, manifest)
        result[path.parent.name] = manifest
    return result


def _validate_manifest(work: Path, manifest: dict[str, Any]) -> None:
    missing = sorted(_REQUIRED_MANIFEST_KEYS - manifest.keys())
    if missing:
        raise ValueError(f"{work.name}/recipe.toml missing fields: {missing}")
    recipe_id = manifest["id"]
    if (
        not isinstance(recipe_id, str)
        or not recipe_id
        or any(
            not (character.islower() or character.isdigit() or character == "-")
            for character in recipe_id
        )
    ):
        raise ValueError(f"{work.name}: id must use lowercase letters, digits, hyphens")
    for field in ("title", "script", "summary"):
        if not isinstance(manifest[field], str) or not manifest[field].strip():
            raise ValueError(f"{work.name}: {field} must be a non-empty string")
    script = work / manifest["script"]
    if not script.is_file():
        raise ValueError(f"{work.name}: script does not exist: {manifest['script']}")
    for field in ("features", "backends", "inputs", "outputs"):
        if not isinstance(manifest[field], list) or not manifest[field]:
            raise ValueError(f"{work.name}: {field} must be a non-empty array")
    input_ids: set[str] = set()
    for item in manifest["inputs"]:
        if not isinstance(item, dict) or not {"id", "path", "geometry"} <= item.keys():
            raise ValueError(f"{work.name}: each input needs id, path, geometry")
        if item["id"] in input_ids:
            raise ValueError(f"{work.name}: duplicate input id {item['id']!r}")
        input_ids.add(item["id"])
        if not (work / item["path"]).is_file():
            raise ValueError(f"{work.name}: input does not exist: {item['path']}")
        for attribute in item.get("attributes", []):
            if not {"name", "element", "channels", "usage"} <= attribute.keys():
                raise ValueError(
                    f"{work.name}: input attributes need name, element, channels, usage"
                )
    output_kinds: set[str] = set()
    for output in manifest["outputs"]:
        if (
            not isinstance(output, dict)
            or not {"path", "kind", "backend"} <= output.keys()
        ):
            raise ValueError(f"{work.name}: each output needs path, kind, backend")
        if output["backend"] not in manifest["backends"]:
            raise ValueError(
                f"{work.name}: output backend {output['backend']!r} is undeclared"
            )
        if output["kind"] not in {"image", "interactive"}:
            raise ValueError(f"{work.name}: unknown output kind {output['kind']!r}")
        output_kinds.add(output["kind"])
        expected_suffix = ".webp" if output["kind"] == "image" else ".html"
        if Path(output["path"]).suffix.lower() != expected_suffix:
            raise ValueError(
                f"{work.name}: {output['kind']} output must use {expected_suffix}: "
                f"{output['path']}"
            )
    missing_kinds = {"image", "interactive"} - output_kinds
    if missing_kinds:
        raise ValueError(
            f"{work.name}: outputs must include image and interactive formats; "
            f"missing {sorted(missing_kinds)}"
        )


def _attribute_contract(summary: Any, expected: dict[str, Any], recipe: str) -> None:
    try:
        actual = summary.attribute(expected["name"])
    except KeyError as exc:
        available = [attribute.name for attribute in summary.attributes]
        raise ValueError(
            f"{recipe}: missing attribute {expected['name']!r}; available: {available}"
        ) from exc
    checks = {
        "element": actual.element,
        "channels": actual.channels,
        "usage": actual.usage,
    }
    for field, value in checks.items():
        if value != expected[field]:
            raise ValueError(
                f"{recipe}: attribute {actual.name!r} {field} is {value!r}, "
                f"expected {expected[field]!r}"
            )


def _inspect_contracts(
    manifest: dict[str, Any], namespace: dict[str, Any], *, write: bool
) -> dict[str, Any]:
    import hakowan as hkw

    sources = namespace.get("RECIPE_INSPECTIONS")
    if not isinstance(sources, dict):
        raise ValueError("recipe script must define RECIPE_INSPECTIONS")
    expected_ids = {item["id"] for item in manifest["inputs"]}
    if set(sources) != expected_ids:
        raise ValueError(
            f"RECIPE_INSPECTIONS keys {sorted(sources)} != manifest inputs {sorted(expected_ids)}"
        )
    payload: dict[str, Any] = {}
    for item in manifest["inputs"]:
        summary = hkw.inspect(sources[item["id"]])
        for attribute in item.get("attributes", []):
            _attribute_contract(summary, attribute, manifest["id"])
        payload[item["id"]] = summary.to_dict()
    if write:
        _write_json(Path("artifacts/inspect.json"), payload)
    return payload


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _source_records(work: Path, manifest: dict[str, Any]) -> list[dict[str, Any]]:
    """Hash code, manifest, and input data affecting generated artifacts."""
    paths = {work / "recipe.toml", *work.glob("*.py")}
    data_dir = work / "data"
    if data_dir.is_dir():
        paths.update(path for path in data_dir.rglob("*") if path.is_file())
    records = []
    for path in sorted(paths):
        records.append(
            {
                "path": path.relative_to(work).as_posix(),
                "bytes": path.stat().st_size,
                "sha256": _sha256(path),
            }
        )
    return records


def _artifact_paths(work: Path) -> dict[str, Path]:
    return {
        name: work / "artifacts" / f"{name}.json"
        for name in ("inspect", "figure", "validation", "render")
    }


def _check_artifacts(work: Path, manifest: dict[str, Any]) -> None:
    """Reject missing, stale, inconsistent, or manually modified artifacts."""
    paths = _artifact_paths(work)
    missing = [
        path.relative_to(work).as_posix()
        for path in paths.values()
        if not path.is_file()
    ]
    if missing:
        raise ValueError(f"{work.name}: missing artifacts {missing}")
    payloads = {
        name: json.loads(path.read_text(encoding="utf-8"))
        for name, path in paths.items()
    }
    expected_inputs = {item["id"] for item in manifest["inputs"]}
    if set(payloads["inspect"]) != expected_inputs:
        raise ValueError(
            f"{work.name}: inspect artifact IDs do not match manifest inputs"
        )
    validation = payloads["validation"]
    if not validation.get("valid") or not validation.get("strict"):
        raise ValueError(f"{work.name}: validation artifact is not strict and valid")
    render = payloads["render"]
    if render.get("recipe") != manifest["id"]:
        raise ValueError(f"{work.name}: render artifact has the wrong recipe ID")
    expected_sources = _source_records(work, manifest)
    if render.get("sources") != expected_sources:
        raise ValueError(
            f"{work.name}: source files changed; run "
            f"python gallery/render_gallery.py --artifacts {work.name}"
        )
    if render.get("artifact_format_version") != ARTIFACT_FORMAT_VERSION:
        raise ValueError(f"{work.name}: artifact format is stale; regenerate artifacts")
    declared = {item["path"] for item in manifest["outputs"]}
    recorded = {item["path"] for item in render.get("outputs", [])}
    if declared != recorded:
        raise ValueError(f"{work.name}: render outputs do not match recipe.toml")
    for item in render["outputs"]:
        path = work / item["path"]
        if not path.is_file():
            raise ValueError(f"{work.name}: output does not exist: {item['path']}")
        if item.get("sha256") != _sha256(path):
            raise ValueError(
                f"{work.name}: output changed: {item['path']}; regenerate artifacts"
            )


def _write_json(path: str | Path, value: Any) -> None:
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def _generate_artifacts(
    work: Path, manifest: dict[str, Any], namespace: dict[str, Any]
) -> None:
    import hakowan as hkw

    figure = namespace.get("RECIPE_FIGURE")
    if figure is None:
        raise ValueError(f"{work.name}: recipe script must define RECIPE_FIGURE")
    inspections = _inspect_contracts(manifest, namespace, write=True)
    data_ids = namespace.get("RECIPE_DATA_IDS")
    function_ids = namespace.get("RECIPE_FUNCTION_IDS")
    spec = hkw.to_spec(figure, data_ids=data_ids, function_ids=function_ids)
    Path("artifacts").mkdir(exist_ok=True)
    Path("artifacts/figure.json").write_text(
        spec.to_json(indent=2) + "\n", encoding="utf-8"
    )
    rebuilt = hkw.from_spec(
        spec,
        data_resolver=namespace.get(
            "RECIPE_DATA_RESOLVER", namespace.get("RECIPE_INSPECTIONS")
        ),
        base_dir=work,
    )
    rebuilt_spec = hkw.to_spec(rebuilt, data_ids=data_ids, function_ids=function_ids)
    if rebuilt_spec.to_json(canonical=True) != spec.to_json(canonical=True):
        raise ValueError(f"{work.name}: canonical specification does not round-trip")
    backend = manifest["backends"][0]
    report = hkw.validate(figure, backend=backend, strict=True)
    report.raise_for_errors()
    _write_json("artifacts/validation.json", report.to_dict())
    outputs = []
    for declaration in manifest["outputs"]:
        path = Path(declaration["path"])
        outputs.append(
            {
                **declaration,
                "exists": path.is_file(),
                "bytes": path.stat().st_size if path.is_file() else None,
                "sha256": _sha256(path) if path.is_file() else None,
            }
        )
    _write_json(
        "artifacts/render.json",
        {
            "recipe": manifest["id"],
            "artifact_format_version": ARTIFACT_FORMAT_VERSION,
            "hakowan_version": hkw.__version__,
            "schema_version": spec.version,
            "input_ids": sorted(inspections),
            "sources": _source_records(work, manifest),
            "outputs": outputs,
        },
    )
    print(f"artifacts: {work.name}/artifacts")


def _run_one(
    folder: str,
    force_backend: str | None = None,
    *,
    check: bool = False,
    artifacts: bool = False,
    similarity_threshold: float = 0.995,
    force_image_updates: bool = False,
) -> None:
    """Run, validate, or generate artifacts for one isolated recipe."""
    import hakowan as hkw
    from PIL import Image

    work = (GALLERY / folder).resolve()
    manifest_path = work / "recipe.toml"
    if not manifest_path.is_file():
        raise ValueError(f"{folder}: recipe.toml is required")
    manifest = tomllib.loads(manifest_path.read_text(encoding="utf-8"))
    _validate_manifest(work, manifest)
    script = manifest["script"]

    os.chdir(work)
    sys.path.insert(0, str(work))
    with tempfile.TemporaryDirectory(prefix=".gallery-candidates-", dir=work) as temp:
        candidate_root = Path(temp)
        converted_outputs: list[tuple[Path, Path]] = []
        candidate_outputs: dict[Path, Path] = {}
        original_render = hkw.render

        def managed_render(root, config=None, filename=None, backend=None, **kwargs):
            selected_backend = backend or force_backend
            if check or artifacts:
                capabilities = hkw.backend_capabilities(selected_backend)
                report = hkw.validate(root, backend=selected_backend, strict=True)
                if config is not None:
                    unsupported = config.render_passes - capabilities.render_passes
                    if unsupported:
                        raise ValueError(
                            f"Backend '{capabilities.name}' does not support render "
                            f"passes {sorted(unsupported)}"
                        )
                report.raise_for_errors()
                for diagnostic in report.warnings:
                    print(
                        f"warning: {filename}: {diagnostic.path}: {diagnostic.message}"
                    )
                print(f"checked: {filename} [{capabilities.name}]")
                return hkw.RenderResult(backend=capabilities.name)

            output_filename = filename
            if filename is not None and Path(filename).suffix.lower() == ".webp":
                requested_path = Path(filename)
                target_path = (
                    requested_path
                    if requested_path.is_absolute()
                    else work / requested_path
                ).resolve()
                if target_path.is_relative_to(work):
                    candidate_path = candidate_outputs.get(target_path)
                    if candidate_path is None:
                        candidate_path = candidate_root / (
                            f"{len(candidate_outputs):04d}{requested_path.suffix.lower()}"
                        )
                        candidate_outputs[target_path] = candidate_path
                    output_filename = candidate_path

            if (
                backend is None
                and selected_backend == "mitsuba"
                and output_filename is not None
            ):
                requested_path = Path(output_filename)
                output_filename = requested_path.with_suffix(".png")
                if requested_path.suffix.lower() == ".webp":
                    conversion = (output_filename, requested_path)
                    if conversion not in converted_outputs:
                        converted_outputs.append(conversion)
            return original_render(
                root,
                config,
                filename=output_filename,
                backend=selected_backend,
                **kwargs,
            )

        hkw.render = managed_render
        try:
            namespace = runpy.run_path(script, run_name="__main__")
        finally:
            hkw.render = original_render

        if check or artifacts:
            _inspect_contracts(manifest, namespace, write=False)
            missing_outputs = [
                output["path"]
                for output in manifest["outputs"]
                if not Path(output["path"]).is_file()
            ]
            if missing_outputs:
                raise ValueError(
                    f"{folder}: declared outputs are missing: {missing_outputs}"
                )
        if artifacts:
            _generate_artifacts(work, manifest, namespace)

        for png, webp in converted_outputs:
            with Image.open(png) as image:
                image.save(webp, "WEBP", quality=WEBP_QUALITY, method=6)

        if not check and not artifacts:
            import numpy as np

            for target_path, candidate_path in candidate_outputs.items():
                if not candidate_path.is_file():
                    continue
                if force_image_updates or not target_path.is_file():
                    target_path.parent.mkdir(parents=True, exist_ok=True)
                    os.replace(candidate_path, target_path)
                    print(f"updated image: {target_path.relative_to(work)}")
                    continue

                if target_path.read_bytes() == candidate_path.read_bytes():
                    print(f"unchanged image: {target_path.relative_to(work)}")
                    continue

                with Image.open(candidate_path) as image:
                    candidate_rgba = np.asarray(image.convert("RGBA"), dtype=np.float32)
                try:
                    with Image.open(target_path) as image:
                        previous_rgba = np.asarray(
                            image.convert("RGBA"), dtype=np.float32
                        )
                except (OSError, ValueError):
                    previous_rgba = None

                score = None
                if (
                    previous_rgba is not None
                    and previous_rgba.shape == candidate_rgba.shape
                ):
                    score = _structural_similarity(previous_rgba, candidate_rgba)

                if score is not None and score >= similarity_threshold:
                    print(
                        f"kept image: {target_path.relative_to(work)} "
                        f"(SSIM {score:.6f})"
                    )
                    continue

                target_path.parent.mkdir(parents=True, exist_ok=True)
                os.replace(candidate_path, target_path)
                detail = (
                    f"SSIM {score:.6f}"
                    if score is not None
                    else "different dimensions or unreadable previous image"
                )
                print(f"updated image: {target_path.relative_to(work)} ({detail})")

        results = work / "results"
        missing_formats = [
            suffix
            for suffix in (".webp", ".html")
            if not any(results.glob(f"*{suffix}"))
        ]
        if missing_formats:
            raise ValueError(
                f"{folder}: results must include WebP and HTML outputs; "
                f"missing {missing_formats}"
            )


def _update_recipe_readme(folder: str, manifest: dict[str, Any]) -> None:
    path = GALLERY / folder / "README.md"
    text = path.read_text(encoding="utf-8").rstrip()
    marker = "## Input contract"
    if marker in text:
        text = text.split(marker, 1)[0].rstrip()
    contracts = []
    for item in manifest["inputs"]:
        attributes = item.get("attributes", [])
        if attributes:
            fields = ", ".join(
                f"`{attribute['name']}` ({attribute['element']} "
                f"{attribute['channels']}-channel {attribute['usage']})"
                for attribute in attributes
            )
        else:
            fields = "no pre-existing attributes required"
        contracts.append(
            f"- `{item['id']}`: {item['geometry']} from `{item['path']}`; {fields}."
        )
    section = [
        "",
        marker,
        "",
        *contracts,
        "",
        "## Reproduce and inspect",
        "",
        "```sh",
        f"python ../render_gallery.py --check {folder}",
        f"python ../render_gallery.py --artifacts {folder}",
        "```",
        "",
        f"[Python]({manifest['script']}) · [Manifest](recipe.toml) · "
        "[Inspection](artifacts/inspect.json) · "
        "[Canonical JSON](artifacts/figure.json) · "
        "[Validation](artifacts/validation.json)",
    ]
    path.write_text(text + "\n" + "\n".join(section) + "\n", encoding="utf-8")


def _generate_index(manifests: dict[str, dict[str, Any]]) -> None:
    by_feature: dict[str, list[tuple[str, dict[str, Any]]]] = {}
    rows = []
    for folder, manifest in sorted(
        manifests.items(), key=lambda item: item[1]["title"]
    ):
        _update_recipe_readme(folder, manifest)
        output = manifest["outputs"][0]["path"]
        rows.append(
            f"| [{manifest['title']}]({folder}/README.md) | "
            f"`{', '.join(manifest['features'])}` | "
            f"`{', '.join(manifest['backends'])}` | [{Path(output).name}]({folder}/{output}) |"
        )
        for feature in manifest["features"]:
            by_feature.setdefault(feature, []).append((folder, manifest))
    lines = [
        "# Hakowan Gallery",
        "",
        "Generated from `recipe.toml` manifests. See [the manifest contract](RECIPE_MANIFEST.md).",
        "",
        "## Recipes",
        "",
        "| Recipe | Features | Backends | Result |",
        "|---|---|---|---|",
        *rows,
        "",
        "## Features",
        "",
    ]
    for feature in sorted(by_feature):
        links = ", ".join(
            f"[{manifest['title']}]({folder}/README.md)"
            for folder, manifest in by_feature[feature]
        )
        lines.append(f"- **{feature}**: {links}")
    (GALLERY / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"index: {GALLERY / 'README.md'}")


def _structural_similarity(reference: Any, candidate: Any) -> float:
    """Compute sampled, Gaussian-windowed SSIM over equally sized RGBA arrays."""
    import numpy as np

    window_size = 11
    stride = 8
    sigma = 1.5
    padding = window_size // 2
    reference = reference.astype(np.float32, copy=False) - 128.0
    candidate = candidate.astype(np.float32, copy=False) - 128.0
    if min(reference.shape[:2]) < window_size:
        pad_width = ((padding, padding), (padding, padding), (0, 0))
        reference = np.pad(reference, pad_width, mode="edge")
        candidate = np.pad(candidate, pad_width, mode="edge")

    ref_windows = np.lib.stride_tricks.sliding_window_view(
        reference, (window_size, window_size), axis=(0, 1)
    )[::stride, ::stride]
    candidate_windows = np.lib.stride_tricks.sliding_window_view(
        candidate, (window_size, window_size), axis=(0, 1)
    )[::stride, ::stride]

    coordinates = np.arange(window_size, dtype=np.float64) - padding
    gaussian = np.exp(-0.5 * (coordinates / sigma) ** 2)
    weights = np.outer(gaussian, gaussian)
    weights /= weights.sum()

    def weighted_sum(windows: Any) -> Any:
        return np.einsum("...ij,ij->...", windows, weights, optimize=True)

    def weighted_product_sum(left: Any, right: Any) -> Any:
        return np.einsum("...ij,...ij,ij->...", left, right, weights, optimize=False)

    mean_ref_centered = weighted_sum(ref_windows)
    mean_candidate_centered = weighted_sum(candidate_windows)
    variance_ref = np.maximum(
        weighted_product_sum(ref_windows, ref_windows)
        - mean_ref_centered * mean_ref_centered,
        0.0,
    )
    variance_candidate = np.maximum(
        weighted_product_sum(candidate_windows, candidate_windows)
        - mean_candidate_centered * mean_candidate_centered,
        0.0,
    )
    covariance = (
        weighted_product_sum(ref_windows, candidate_windows)
        - mean_ref_centered * mean_candidate_centered
    )
    mean_ref = mean_ref_centered + 128.0
    mean_candidate = mean_candidate_centered + 128.0

    c1 = (0.01 * 255) ** 2
    c2 = (0.03 * 255) ** 2
    numerator = (2 * mean_ref * mean_candidate + c1) * (2 * covariance + c2)
    denominator = (mean_ref**2 + mean_candidate**2 + c1) * (
        variance_ref + variance_candidate + c2
    )
    return float(np.clip(numerator / denominator, -1.0, 1.0).mean())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("examples", nargs="*", metavar="EXAMPLE")
    parser.add_argument("--force-backend", choices=("webgl", "mitsuba", "blender"))
    parser.add_argument(
        "--check", action="store_true", help="validate without rendering"
    )
    parser.add_argument(
        "--artifacts",
        action="store_true",
        help="validate recipes and generate canonical artifacts",
    )
    parser.add_argument(
        "--check-artifacts",
        action="store_true",
        help="verify checked-in artifacts match code, data, and outputs",
    )
    parser.add_argument(
        "--similarity-threshold",
        type=float,
        default=0.995,
        help="SSIM score at or above which images are retained during rendering",
    )
    parser.add_argument(
        "--force-image-updates",
        action="store_true",
        help="replace rendered WebP files even when SSIM marks them similar",
    )
    parser.add_argument(
        "--index", action="store_true", help="generate gallery/README.md"
    )
    parser.add_argument("--one", metavar="EXAMPLE", help=argparse.SUPPRESS)
    args = parser.parse_args()
    if not 0.0 <= args.similarity_threshold <= 1.0:
        parser.error("--similarity-threshold must be between 0 and 1")
    if args.force_image_updates and (
        args.check or args.artifacts or args.check_artifacts or args.index
    ):
        parser.error(
            "--force-image-updates cannot be combined with check, artifacts, or index options"
        )

    manifests = _manifests()
    known = sorted(manifests)
    unknown = [target for target in args.examples if target not in known]
    if unknown:
        parser.error(f"unknown example(s): {unknown}; known examples: {known}")

    if args.index:
        _generate_index(manifests)
    artifact_failures: list[str] = []
    if args.check_artifacts:
        targets = args.examples or sorted(manifests)
        for folder in targets:
            try:
                _check_artifacts(GALLERY / folder, manifests[folder])
            except Exception as error:
                artifact_failures.append(folder)
                print(f"stale: {folder}: {error}", file=sys.stderr)
            else:
                print(f"fresh: {folder}")
    if (
        (args.index or args.check_artifacts)
        and not args.check
        and not args.artifacts
        and args.force_backend is None
    ):
        return 1 if artifact_failures else 0
    if args.one is not None:
        _run_one(
            args.one,
            args.force_backend,
            check=args.check,
            artifacts=args.artifacts,
            similarity_threshold=args.similarity_threshold,
            force_image_updates=args.force_image_updates,
        )
        return 0

    targets = args.examples or (sorted(manifests) if args.artifacts else known)

    failures: list[str] = []
    for folder in targets:
        print(f"\n=== {folder} ===", flush=True)
        started = time.time()
        command = [sys.executable, str(GALLERY / "render_gallery.py"), "--one", folder]
        if args.force_backend is not None:
            command.extend(("--force-backend", args.force_backend))
        if args.check:
            command.append("--check")
        if args.artifacts:
            command.append("--artifacts")
        command.extend(("--similarity-threshold", str(args.similarity_threshold)))
        if args.force_image_updates:
            command.append("--force-image-updates")
        process = subprocess.run(command, cwd=GALLERY / folder)
        duration = time.time() - started
        status = (
            "ok" if process.returncode == 0 else f"FAILED (exit {process.returncode})"
        )
        if process.returncode != 0:
            failures.append(folder)
        print(f"--- {folder}: {status} in {duration:.1f}s", flush=True)

    print(f"\nDone. {len(targets) - len(failures)}/{len(targets)} succeeded.")
    if failures:
        print(f"Failed: {failures}")
    if artifact_failures:
        print(f"Stale artifacts: {artifact_failures}")
    return 1 if failures or artifact_failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
