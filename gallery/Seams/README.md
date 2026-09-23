# UV Seams

This example extracts discontinuities in an indexed UV attribute and overlays the resulting seam curves on the original surface. `Boundary(attributes=["texcoord"])` unifies the UV index buffer before selecting topological and attribute boundaries.

[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Seams/results/spot_seam.webp?raw=true"/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Seams/results/spot_seam.webp?raw=true)

[Interactive demo](https://qnzhou.github.io/hakowan-gallery/gallery/Seams/results/spot_seam.html)

## Data

The quadrangulated Spot model is by [Keenan Crane](https://www.cs.cmu.edu/~kmcrane/Projects/ModelRepository/) and is released into the public domain. Its indexed `texcoord` attribute defines the UV seams.

## Input contract

- `mesh`: surface from `data/spot_quadrangulated.obj`; `texcoord` (indexed 2-channel uv).

## Reproduce and inspect

```sh
python ../render_gallery.py --check Seams
python ../render_gallery.py --artifacts Seams
```

[Python](seam.py) · [Manifest](recipe.toml) · [Inspection](artifacts/inspect.json) · [Canonical JSON](artifacts/figure.json) · [Validation](artifacts/validation.json)
