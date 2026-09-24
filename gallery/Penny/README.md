# Penny

This example visualizes the normal and depth fields of a reconstructed penny model.

[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Penny/results/penny.webp?raw=true" width=45%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Penny/results/penny.webp?raw=true)
[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Penny/results/penny_normal.webp?raw=true" width=45%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Penny/results/penny_normal.webp?raw=true)

[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Penny/results/penny_depth.webp?raw=true" width=45%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Penny/results/penny_depth.webp?raw=true)
[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Penny/results/penny_albedo.webp?raw=true" width=45%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Penny/results/penny_albedo.webp?raw=true)

[Interactive demo](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Penny/results/penny.html)

## Data

The data used in this model is generated from [depth map images from GIGAmacro](https://viewer.gigamacro.com/view/71fde4b511d19569?x1=23537.00&y1=-23808.00&res1=47.14&rot1=0.00). It is converted to mesh using [project Lagrange](https://opensource.adobe.com/lagrange-docs/).

## Input contract

- `mesh`: surface from `data/penny.glb`; no pre-existing attributes required.

## Reproduce and inspect

```sh
python ../render_gallery.py --check Penny
python ../render_gallery.py --artifacts Penny
```

[Python](penny.py) · [Manifest](recipe.toml) · [Inspection](artifacts/inspect.json) · [Canonical JSON](artifacts/figure.json) · [Validation](artifacts/validation.json)
