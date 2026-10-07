# Box

This example colors the six faces of a box by `facet_id`, overlays the polygon edges as a black wireframe, and labels each face with a world-space annotation. An orthographic camera shows the front, top, and right faces.

[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Box/results/box.webp?raw=true"/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Box/results/box.webp?raw=true)

[Interactive demo](https://qnzhou.github.io/hakowan-gallery/gallery/Box/results/box.html)

## Data

The bundled [`data/box.msh`](data/box.msh) contains a unit cube centered at the origin, with eight vertices and six quadrilateral faces. Its facet-domain scalar attribute `facet_id` stores values from 0 to 5 for categorical coloring; no preprocessing is required. No external source or data-specific license is recorded for this mesh.

## Input contract

- `mesh`: surface from `data/box.msh`; `facet_id` (facet 1-channel scalar).

## Reproduce and inspect

```sh
python ../render_gallery.py --check Box
python ../render_gallery.py --artifacts Box
```

[Python](box.py) · [Manifest](recipe.toml) · [Inspection](artifacts/inspect.json) · [Canonical JSON](artifacts/figure.json) · [Validation](artifacts/validation.json)
