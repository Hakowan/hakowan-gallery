# Tetrahedral Meshing in the Wild

This example tries to reproduce the rendering style used in the paper "[Tetrahedral Meshing in the
Wild](https://yixin-hu.github.io/tetwild.pdf)". It shows the surface triangulation of a tet mesh as
well as a cut-away view of the internal tet shapes.

[<img width=32% src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/TetWild/results/bust_bd.png?raw=true"/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/TetWild/results/bust_bd.png?raw=true)
[<img width=32% src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/TetWild/results/bust_clipped.png?raw=true"/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/TetWild/results/bust_clipped.png?raw=true)
[<img width=32% src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/TetWild/results/bust_clipped2.png?raw=true"/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/TetWild/results/bust_clipped2.png?raw=true)

[<img width=90% src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/TetWild/results/bust.png?raw=true"/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/TetWild/results/bust.png?raw=true)

## Data

The data used in this example is with the [TetWild](https://github.com/Yixin-Hu/TetWild) code with
default parameters.

```sh
./TetWild bust.obj bust.msh
```

The bust sculpture shape used is design by [Luke Chilson](https://www.thingiverse.com/lukechilson/designs) and published on [Thingiverse](https://www.thingiverse.com/thing:14565).
