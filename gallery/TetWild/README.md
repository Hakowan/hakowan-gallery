# Tetrahedral Meshing in the Wild

This example tries to reproduce the rendering style used in the paper "[Tetrahedral Meshing in the
Wild](https://yixin-hu.github.io/tetwild.pdf)". It shows the surface triangulation of a tet mesh as
well as a cut-away view of the internal tet shapes.

[<img width=32% src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/TetWild/results/bust_bd.webp?raw=true"/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/TetWild/results/bust_bd.webp?raw=true)
[<img width=32% src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/TetWild/results/bust_clipped.webp?raw=true"/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/TetWild/results/bust_clipped.webp?raw=true)
[<img width=32% src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/TetWild/results/bust_clipped2.webp?raw=true"/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/TetWild/results/bust_clipped2.webp?raw=true)

[<img width=90% src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/TetWild/results/bust.webp?raw=true"/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/TetWild/results/bust.webp?raw=true)

[Interactive demo](https://qnzhou.github.io/hakowan-gallery/gallery/TetWild/results/bust.html)

## Data

The data used in this example is with the [TetWild](https://github.com/Yixin-Hu/TetWild) code with
default parameters.

```sh
./TetWild bust.obj bust.msh
```

The bust sculpture shape used is design by [Luke Chilson](https://www.thingiverse.com/lukechilson/designs) and published on [Thingiverse](https://www.thingiverse.com/thing:14565).

## Input contract

- `tetrahedral`: tetrahedral from `data/bust.msh`; no pre-existing attributes required.

## Reproduce and inspect

```sh
python ../render_gallery.py --check TetWild
python ../render_gallery.py --artifacts TetWild
```

[Python](tetwild.py) · [Manifest](recipe.toml) · [Inspection](artifacts/inspect.json) · [Canonical JSON](artifacts/figure.json) · [Validation](artifacts/validation.json)
