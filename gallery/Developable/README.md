# Developability of Triangle Meshes

This example tries to replicte Figure 1 from the paper "[Developability of Triangle Meshes](https://odedstein.com/projects/developability/)".

[<img width=45% src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Developable/results/mask_0.webp?raw=true"/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Developable/results/mask_0.webp?raw=true)
[<img width=45% src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Developable/results/mask_1.webp?raw=true"/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Developable/results/mask_1.webp?raw=true)

[<img width=45% src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Developable/results/mask_2.webp?raw=true"/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Developable/results/mask_2.webp?raw=true)
[<img width=45% src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Developable/results/mask_3.webp?raw=true"/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Developable/results/mask_3.webp?raw=true)

[Interactive demo](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Developable/results/mask.html) 

## Data

The data used in this example is from the [data](https://www.cs.cmu.edu/~kmcrane/Projects/DiscreteDevelopable/discrete-developable-data.zip) released by the paper authors.

## Input contract

- `mesh`: surface from `data/mask_triangulated.obj`; no pre-existing attributes required.

## Reproduce and inspect

```sh
python ../render_gallery.py --check Developable
python ../render_gallery.py --artifacts Developable
```

[Python](developable.py) · [Manifest](recipe.toml) · [Inspection](artifacts/inspect.json) · [Canonical JSON](artifacts/figure.json) · [Validation](artifacts/validation.json)
