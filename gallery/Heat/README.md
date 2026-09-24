# The Heat Method

This example reproduced [this
figure](https://www.cs.cmu.edu/~kmcrane/Projects/HeatMethod/teaser.png) from the paper "[The Heat
Method for Distance Computation](https://www.cs.cmu.edu/~kmcrane/Projects/HeatMethod/index.html)".

[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Heat/results/bunny_heat.webp?raw=true" width=45%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Heat/results/bunny_heat.webp?raw=true)
[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Heat/results/bunny_heat_back.webp?raw=true" width=45%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Heat/results/bunny_heat_back.webp?raw=true)

[Interactive demo](https://qnzhou.github.io/hakowan-gallery/gallery/Heat/results/bunny_heat.html)

## Data

The distance field is computed using
[`heat_geodesic`](https://libigl.github.io/libigl-python-bindings/igl_docs/#heat_geodesic) method
from libigl. The field is stored as `dist` field in [data/bunny_heat.ply](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Heat/data/bunny_heat.ply).

## Input contract

- `mesh`: surface from `data/bunny_heat.ply`; `dist` (indexed 1-channel scalar).

## Reproduce and inspect

```sh
python ../render_gallery.py --check Heat
python ../render_gallery.py --artifacts Heat
```

[Python](heat.py) · [Manifest](recipe.toml) · [Inspection](artifacts/inspect.json) · [Canonical JSON](artifacts/figure.json) · [Validation](artifacts/validation.json)
