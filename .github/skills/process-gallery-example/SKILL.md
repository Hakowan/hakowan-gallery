---
name: process-gallery-example
description: Prepare new or changed Hakowan Gallery examples for review by completing recipe manifests and README content, generating canonical artifacts, refreshing the gallery index, and verifying freshness. Use when adding, importing, migrating, or updating folders under gallery/.
---

# Process a Hakowan Gallery example

Turn each new example into a source-backed, reproducible gallery recipe. Preserve the author's visualization and data. Do not replace working example logic with a simplified demonstration.

## Source of truth

Read these before editing:

- `gallery/RECIPE_MANIFEST.md` for the manifest contract.
- `gallery/render_gallery.py` for generation and freshness behavior.
- One existing recipe with similar data and output types.

The source recipe lives in `gallery/<Folder>/`. Files under `artifacts/` and generated README sections are derived output. Never hand-edit artifact JSON.

## 1. Discover incomplete examples

Inspect repository status and identify new or changed folders under `gallery/`. For each target, inventory:

- executable Python scripts;
- files under `data/`;
- existing files under `results/`;
- `README.md`, `recipe.toml`, and `artifacts/` presence;
- accidental duplicate or misspelled directories.

Treat unrelated changes as user work. Do not delete or rewrite them.

## 2. Inspect the actual input contract

Run Hakowan inspection on every declared input; never infer attribute names or domains from script text:

```sh
PYTHONPATH=../hakowan/src python -c \
  'import hakowan as h, json; print(json.dumps(h.inspect("gallery/<Folder>/data/<file>").to_dict(), indent=2))'
```

Record only attributes the recipe actually requires. For every required attribute capture:

- exact name;
- element domain: `vertex`, `facet`, `corner`, or `indexed`;
- channel count;
- usage such as `scalar`, `vector`, `normal`, `uv`, or `color`.

## 3. Make the script artifact-compatible

The recipe script must expose:

```python
RECIPE_FIGURE = figure
RECIPE_INSPECTIONS = {"<input-id>": source}
```

`RECIPE_INSPECTIONS` keys must exactly match the manifest input IDs. Add `RECIPE_DATA_IDS`, `RECIPE_FUNCTION_IDS`, or `RECIPE_DATA_RESOLVER` only when canonical serialization genuinely requires them.

Declare at least one static WebP result and one interactive HTML result. Result paths in the script and manifest must match exactly. Keep rendering in a `__main__` guard when practical, but keep figure construction and recipe globals importable.

## 4. Create `recipe.toml`

Use a repository-unique lowercase hyphenated ID:

```toml
id = "example-id"
title = "Human-readable title"
script = "example.py"
summary = "One sentence describing the visualization intent."
features = ["surface", "curve"]
backends = ["mitsuba", "webgl"]

[[inputs]]
id = "mesh"
path = "data/model.ext"
geometry = "surface"

[[inputs.attributes]]
name = "required_field"
element = "facet"
channels = 3
usage = "vector"

[[outputs]]
path = "results/example.webp"
kind = "image"
backend = "mitsuba"

[[outputs]]
path = "results/example.html"
kind = "interactive"
backend = "webgl"
```

Feature tags must describe observable behavior and support search. Reuse existing tags before introducing synonyms.

## 5. Create the authored README portion

Before the generated contract section, include:

- title;
- concise explanation of what the example demonstrates;
- linked preview image;
- interactive demo link when HTML exists;
- input-data provenance and license when known;
- any preparation method needed to reproduce derived fields.

Use repository-relative GitHub and Pages URLs consistent with existing recipes. Do not manually write or preserve content from `## Input contract` onward; `--index` owns that section.

## 6. Generate artifacts and documentation

From the repository root, with the sibling Hakowan checkout:

```sh
PYTHONPATH=../hakowan/src python gallery/render_gallery.py --artifacts <Folder>
python gallery/render_gallery.py --index
```

Artifact generation must produce:

```text
gallery/<Folder>/artifacts/inspect.json
gallery/<Folder>/artifacts/figure.json
gallery/<Folder>/artifacts/validation.json
gallery/<Folder>/artifacts/render.json
```

Do not fabricate artifacts or copy them from another recipe. If generation fails, fix the source recipe or report the exact reproducible blocker. Do not bypass validation.

## 7. Verify the deliverable

Run:

```sh
python gallery/render_gallery.py --check-artifacts <Folder>
python -m ruff check gallery/<Folder>
python -m ruff format --check gallery/<Folder>
python gallery/render_gallery.py --index
git diff --check
```

For multiple recipes, pass all folders to `--check-artifacts`, then run the repository-wide freshness check before completion:

```sh
python gallery/render_gallery.py --check-artifacts
```

Visually inspect each declared static image. Confirm the gallery index lists every new recipe and feature tag.

## Acceptance criteria

A processed example is complete only when:

- `recipe.toml` validates and paths match real files;
- required input attributes match `hkw.inspect()` output;
- README authored content and generated contract section are present;
- all four artifact JSON files exist;
- `validation.json` is strict and valid with no errors;
- source, data, results, and artifact hashes are fresh;
- static and interactive outputs are declared;
- the generated gallery index contains the recipe;
- lint, formatting, freshness, and diff checks pass.

Keep generated benchmark runs, temporary captures, caches, and publication corpora out of Git. Commit only when requested or when the surrounding task explicitly includes committing the completed recipes.
