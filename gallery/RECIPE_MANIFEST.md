# Recipe manifest contract

Recipes declare machine-readable metadata in `recipe.toml`. The gallery runner validates this contract and uses it to generate artifacts and the gallery index.

## Required fields

```toml
id = "heat-geodesic"
title = "The Heat Method"
script = "heat.py"
summary = "Geodesic distance rendered as color and isocontours."
features = ["scalar-field", "isocontour", "legend"]
backends = ["mitsuba", "webgl"]

[[inputs]]
id = "mesh"
path = "data/bunny_heat.ply"
geometry = "surface"

[[inputs.attributes]]
name = "dist"
element = "vertex"
channels = 1
usage = "scalar"

[[outputs]]
path = "results/bunny_heat.webp"
kind = "image"
backend = "mitsuba"
```

- `id`: repository-unique lowercase identifier using letters, digits, and hyphens.
- `title`: human-readable recipe name.
- `script`: executable Python file beside the manifest.
- `summary`: one-sentence visualization intent.
- `features`: searchable feature tags.
- `backends`: backends intentionally exercised by the recipe.
- `inputs`: source contracts. `path` is relative to the recipe directory.
- `inputs.attributes`: required attribute contracts checked against `hkw.inspect()`.
- `outputs`: expected generated files, their kind (`image` or `interactive`), and backend.
- Every recipe declares at least one static `image` output using `.webp` and one `interactive` output using `.html`.

## Script artifact hooks

A recipe script exposes these module globals:

```python
RECIPE_FIGURE = figure
RECIPE_INSPECTIONS = {"mesh": source}
RECIPE_DATA_IDS = None          # optional mapping/callable for in-memory data
RECIPE_FUNCTION_IDS = None      # optional mapping/callable for trusted callables
```

`RECIPE_INSPECTIONS` keys match manifest input IDs. `render_gallery.py --artifacts` executes the script with rendering intercepted, checks the declared contracts, and writes:

- `artifacts/inspect.json`
- `artifacts/figure.json`
- `artifacts/validation.json`
- `artifacts/render.json`

Artifacts are generated; do not edit them manually.


## Maintenance workflow

When a recipe script, helper module, or file under its `data/` directory changes,
regenerate only that recipe:

```sh
python gallery/render_gallery.py --artifacts RecipeFolder
```

`artifacts/render.json` records SHA-256 hashes for `recipe.toml`, recipe Python
files, every file under `data/`, and every declared output. The fast check:

```sh
python gallery/render_gallery.py --check-artifacts
```

fails with the exact recipe regeneration command when any source or output is
stale. README-only changes do not require artifact regeneration.

The `Check gallery` GitHub Actions workflow verifies artifact freshness and
regenerates the documentation index to ensure checked-in documentation remains
current.
