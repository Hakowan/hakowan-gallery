# Mesh deformation

This example aims to visualize the deformed surface that are k-harmonic with k=1,2,3 and 4.
This example is inspired by figure 2 from the paper "[An Intuitive Framework for Real-Time Freeform Modeling](https://www.graphics.rwth-aachen.de/media/papers/modeling1.pdf)".


[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Deformation/results/cylinder_1.webp?raw=true" width=45%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Deformation/results/cylinder_1.webp?raw=true)
[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Deformation/results/cylinder_2.webp?raw=true" width=45%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Deformation/results/cylinder_2.webp?raw=true)
[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Deformation/results/cylinder_3.webp?raw=true" width=45%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Deformation/results/cylinder_3.webp?raw=true)
[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Deformation/results/cylinder_4.webp?raw=true" width=45%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Deformation/results/cylinder_4.webp?raw=true)

[Interactive demo](https://qnzhou.github.io/hakowan-gallery/gallery/Deformation/results/cylinders.html)

## Data

The input [cylinder](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Deformation/data/cylinder.ply) is generate with Blender, and its deformed shapes are generated using the script
[deform.py](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Deformation/deform.py).

## Input contract

- `mesh`: surface from `data/cylinder_1.msh`; `label` (facet 1-channel scalar).

## Reproduce and inspect

```sh
python ../render_gallery.py --check Deformation
python ../render_gallery.py --artifacts Deformation
```

[Python](render.py) · [Manifest](recipe.toml) · [Inspection](artifacts/inspect.json) · [Canonical JSON](artifacts/figure.json) · [Validation](artifacts/validation.json)
