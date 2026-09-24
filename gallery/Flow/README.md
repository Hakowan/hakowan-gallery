# Mean Curvature Flow

This example visualize the mean curvature flow of a bust sculpture.
In addition to the shapes, we also visualize the distance to the origin mesh using color.

[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Flow/results/bust_00.webp?raw=true" width=22%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Flow/results/bust_00.webp?raw=true)
[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Flow/results/bust_02.webp?raw=true" width=22%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Flow/results/bust_02.webp?raw=true)
[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Flow/results/bust_05.webp?raw=true" width=22%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Flow/results/bust_05.webp?raw=true)
[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Flow/results/bust_09.webp?raw=true" width=22%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Flow/results/bust_09.webp?raw=true)

[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Flow/results/bust_dist_00.webp?raw=true" width=22%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Flow/results/bust_dist_00.webp?raw=true)
[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Flow/results/bust_dist_02.webp?raw=true" width=22%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Flow/results/bust_dist_02.webp?raw=true)
[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Flow/results/bust_dist_05.webp?raw=true" width=22%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Flow/results/bust_dist_05.webp?raw=true)
[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Flow/results/bust_dist_09.webp?raw=true" width=22%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Flow/results/bust_dist_09.webp?raw=true)

[Interactive demo](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Flow/results/bust_all.html)

## Data

The bust sculpture used is design by [Luke Chilson](https://www.thingiverse.com/lukechilson/designs) and published on [Thingiverse](https://www.thingiverse.com/thing:14565).

## Input contract

- `surface`: surface from `data/flow_00.ply`; `dist` (indexed 1-channel scalar).

## Reproduce and inspect

```sh
python ../render_gallery.py --check Flow
python ../render_gallery.py --artifacts Flow
```

[Python](flow.py) · [Manifest](recipe.toml) · [Inspection](artifacts/inspect.json) · [Canonical JSON](artifacts/figure.json) · [Validation](artifacts/validation.json)
