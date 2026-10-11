# Points

Compare sphere, cube, and disk point marks at the vertices of a subdivided icosphere. Each glyph is oriented by its vertex normal.

[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Points/results/points.webp?raw=true"/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Points/results/points.webp?raw=true)

[Interactive demo](https://qnzhou.github.io/hakowan-gallery/gallery/Points/results/points.html)

## Input contract

- `icosphere`: surface from `data/icosahedron.ply`.

## Reproduce and inspect

```sh
python ../render_gallery.py --check Points
python ../render_gallery.py --artifacts Points
```

[Python](points.py) · [Manifest](recipe.toml) · [Inspection](artifacts/inspect.json) · [Canonical JSON](artifacts/figure.json) · [Validation](artifacts/validation.json)
