# Components

This example illustrates the disconnected components of a given mesh.

[<img width=40% src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Components/results/foot_front.webp?raw=true"/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Components/results/foot_front.webp?raw=true)
[<img width=40% src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Components/results/foot_side.webp?raw=true"/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Components/results/foot_side.webp?raw=true)
[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Components/results/foot_top.webp?raw=true"/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Components/results/foot_top.webp?raw=true)

[Interactive demo](https://qnzhou.github.io/hakowan-gallery/gallery/Components/results/foot.html)

## Data

The data used in this example is from "[Anatomic Human Foot & Lower Extremity Version
2.0](https://www.thingiverse.com/thing:22628)" designed by
[DrGlassDPM](https://www.thingiverse.com/thing:22628) on on Thingiverse. The components can be
computed via Lagrange:

``` py
mesh = lagrange.io.load_mesh("data/foot.msh")
lagrange.compute_components(mesh, output_attribute_name="comp")
```

## Input contract

- `mesh`: surface from `data/foot.ply`; no pre-existing attributes required.

## Reproduce and inspect

```sh
python ../render_gallery.py --check Components
python ../render_gallery.py --artifacts Components
```

[Python](components.py) · [Manifest](recipe.toml) · [Inspection](artifacts/inspect.json) · [Canonical JSON](artifacts/figure.json) · [Validation](artifacts/validation.json)
