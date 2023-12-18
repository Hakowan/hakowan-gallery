# Components

This example illustrates the disconnected components of a given mesh.

[<img width=40% src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Components/results/foot_front.png?raw=true"/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Components/results/foot_front.png?raw=true)
[<img width=40% src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Components/results/foot_side.png?raw=true"/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Components/results/foot_side.png?raw=true)
[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Components/results/foot_top.png?raw=true"/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Components/results/foot_top.png?raw=true)

## Data

The data used in this example is from "[Anatomic Human Foot & Lower Extremity Version
2.0](https://www.thingiverse.com/thing:22628)" designed by
[DrGlassDPM](https://www.thingiverse.com/thing:22628) on on Thingiverse. The components can be
computed via Lagrange:

``` py
mesh = lagrange.io.load_mesh("data/foot.msh")
lagrange.compute_components(mesh, output_attribute_name="comp")
```
