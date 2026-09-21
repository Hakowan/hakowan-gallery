# Powell-Sabin Subdivision

This exmaple visualizes the Powell-Sabin subdivision for tets. A similar figure can be found in
Figure 2.1 and 2.2 in the paper "[A trivariate Powell-Sabin
interpolant](https://www.sciencedirect.com/science/article/pii/0167839688900015)".


[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/PowellSabin/results/powell_sabin.webp?raw=true" width=45%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/PowellSabin/results/powell_sabin.webp?raw=true)
[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/PowellSabin/results/powell_sabin_explode.webp?raw=true" width=45%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/PowellSabin/results/powell_sabin_explode.webp?raw=true)

[Interactive demo](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/PowellSabin/results/powell_sabin.html)

## Data

The data were generated using [this script](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/PowellSabin/generate_data.py).

## Input contract

- `mesh`: surface from `data/powell_sabin.ply`; `vertex_label` (indexed 1-channel scalar).

## Reproduce and inspect

```sh
python ../render_gallery.py --check PowellSabin
python ../render_gallery.py --artifacts PowellSabin
```

[Python](powell_sabin.py) · [Manifest](recipe.toml) · [Inspection](artifacts/inspect.json) · [Canonical JSON](artifacts/figure.json) · [Validation](artifacts/validation.json)
