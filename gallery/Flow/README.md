# Mean Curvature Flow

This example compares the initial and final surfaces of a mean-curvature flow
and visualizes each surface's distance from the original mesh as a scalar field.

[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Flow/results/bust_comp.webp?raw=true" width=90%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Flow/results/bust_comp.webp?raw=true)

[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Flow/results/bust_00.webp?raw=true" width=45%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Flow/results/bust_00.webp?raw=true)
[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Flow/results/bust_09.webp?raw=true" width=45%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Flow/results/bust_09.webp?raw=true)

[Interactive demo](https://qnzhou.github.io/hakowan-gallery/gallery/Flow/results/bust_all.html)

## Data

The bust sculpture was designed by [Luke Chilson](https://www.thingiverse.com/lukechilson/designs)
and published on [Thingiverse](https://www.thingiverse.com/thing:14565). The `dist`
field stores the distance from each flow iterate to the original mesh.

## Input contract

- `initial-surface`: surface from `data/flow_00.ply`; `dist` (indexed 1-channel scalar).
- `final-surface`: surface from `data/flow_09.ply`; `dist` (indexed 1-channel scalar).

## Reproduce and inspect

```sh
python ../render_gallery.py --check Flow
python ../render_gallery.py --artifacts Flow
```

[Python](flow.py) · [Manifest](recipe.toml) · [Inspection](artifacts/inspect.json) · [Canonical JSON](artifacts/figure.json) · [Validation](artifacts/validation.json)
