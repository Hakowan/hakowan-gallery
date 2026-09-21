# Moon

This example aims to generate 3D visualization of both sides of the moon.

[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Moon/results/moon.webp?raw=true" width=45%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Moon/results/moon.webp?raw=true)
[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Moon/results/moon_backside.webp?raw=true" width=45%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Moon/results/moon_backside.webp?raw=true)

[Interactive demo](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Moon/results/moon.html)

## Data

The data used in this example is from NASA's [CGI Moon Kit](https://svs.gsfc.nasa.gov/cgi-bin/details.cgi?aid=4720).

## Input contract

- `mesh`: surface from `data/moon.ply`; no pre-existing attributes required.

## Reproduce and inspect

```sh
python ../render_gallery.py --check Moon
python ../render_gallery.py --artifacts Moon
```

[Python](moon.py) · [Manifest](recipe.toml) · [Inspection](artifacts/inspect.json) · [Canonical JSON](artifacts/figure.json) · [Validation](artifacts/validation.json)
