# Scalable Locally Injective Mappings

This example aims to reproduce Figure 3 and 10 from the paper [Scalable Locally Injective
Mappings](https://cims.nyu.edu/gcl/papers/SLIM2017.pdf).

[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Slim/results/fig3.webp?raw=true" width=45%/>](https://github.com/qnzhou/hakowan-gallery/raw/main/gallery/Slim/results/fig3.webp)
[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Slim/results/fig10.webp?raw=true" width=45%/>](https://github.com/qnzhou/hakowan-gallery/raw/main/gallery/Slim/results/fig10.webp)

[Interactive Figure 3](https://qnzhou.github.io/hakowan-gallery/gallery/Slim/results/fig3.html) · [Interactive Figure 10](https://qnzhou.github.io/hakowan-gallery/gallery/Slim/results/fig10.html)

## Data

The data used in this example is the [official
data](https://cims.nyu.edu/gcl/papers/SLIM2017_Data.zip) released by the authors.

## Input contract

- `mesh`: surface from `data/fig3.obj`; `texcoord` (indexed 2-channel uv).

## Reproduce and inspect

```sh
python ../render_gallery.py --check Slim
python ../render_gallery.py --artifacts Slim
```

[Python](slim.py) · [Manifest](recipe.toml) · [Inspection](artifacts/inspect.json) · [Canonical JSON](artifacts/figure.json) · [Validation](artifacts/validation.json)
