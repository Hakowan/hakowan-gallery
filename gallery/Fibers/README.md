# Fibers

This example visualizes the fibers in a plain-knit fabric.

[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Fibers/results/fibers.webp?raw=true"/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Fibers/results/fibers.webp?raw=true)

[Interactive demo](https://qnzhou.github.io/hakowan-gallery/gallery/Fibers/results/fibers.html)

## Data

The data used in this visualization is generated using the [plain-knit-yarn](https://github.com/keenancrane/plain-knit-yarn) by [Keenan Crane](https://www.cs.cmu.edu/~kmcrane/).

## Input contract

- `fibers`: curve from `data/fibers.obj`; no pre-existing attributes required.

## Reproduce and inspect

```sh
python ../render_gallery.py --check Fibers
python ../render_gallery.py --artifacts Fibers
```

[Python](fibers.py) · [Manifest](recipe.toml) · [Inspection](artifacts/inspect.json) · [Canonical JSON](artifacts/figure.json) · [Validation](artifacts/validation.json)
