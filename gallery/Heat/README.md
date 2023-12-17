# The Heat Method

This example reproduced [this
figure](https://www.cs.cmu.edu/~kmcrane/Projects/HeatMethod/teaser.png) from the paper "[The Heat
Method for Distance Computation](https://www.cs.cmu.edu/~kmcrane/Projects/HeatMethod/index.html)".

[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Heat/results/bunny_heat.png?raw=true"/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Heat/results/bunny_heat.png?raw=true)

## Data

The distance field is computed using
[`heat_geodesic`](https://libigl.github.io/libigl-python-bindings/igl_docs/#heat_geodesic) method
from libigl. The field is stored as `dist` field in [data/bunny_heat.ply](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Heat/data/bunny_heat.ply).
