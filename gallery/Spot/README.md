# Spot

This basic example displays a surface mesh with its polygon edges overlaid as a wireframe.

[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Spot/results/spot_wireframe.webp?raw=true"/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Spot/results/spot_wireframe.webp?raw=true)

[Interactive demo](https://qnzhou.github.io/hakowan-gallery/gallery/Spot/results/spot_wireframe.html)

## Data

The quadrangulated Spot model is by [Keenan Crane](https://www.cs.cmu.edu/~kmcrane/Projects/ModelRepository/) and is released into the public domain.

## Input contract

- `mesh`: surface from `data/spot_quadrangulated.obj`; no pre-existing attributes required.

## Reproduce and inspect

```sh
python ../render_gallery.py --check Spot
python ../render_gallery.py --artifacts Spot
```

[Python](spot.py) · [Manifest](recipe.toml) · [Inspection](artifacts/inspect.json) · [Canonical JSON](artifacts/figure.json) · [Validation](artifacts/validation.json)
