# Topographic Map

This example aims to generate a 3D topographic map from elevation data provided by [USGS](https://www.usgs.gov/the-national-map-data-delivery/gis-data-download).

[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Elevation/results/usgs_1_n35112.webp?raw=true" width=45%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Elevation/results/usgs_1_n35112.webp?raw=true)
[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Elevation/results/usgs_1_n35112_side.webp?raw=true" width=45%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Elevation/results/usgs_1_n35112_side.webp?raw=true)

[Interactive demo](https://qnzhou.github.io/hakowan-gallery/gallery/Elevation/results/usgs_1_n35112.html)

## Data
The [input](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Elevation/data/USGS_1_n35w112.tif) is height field image representing a tile of the US elevation map (N35 and W112) downloaded from USGS. It is converted to a dense quad mesh using [this script](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Elevation/image2mesh.py).

## Input contract

- `terrain`: heightmap from `data/USGS_1_n35w112.tif`; no pre-existing attributes required.

## Reproduce and inspect

```sh
python ../render_gallery.py --check Elevation
python ../render_gallery.py --artifacts Elevation
```

[Python](elevation.py) · [Manifest](recipe.toml) · [Inspection](artifacts/inspect.json) · [Canonical JSON](artifacts/figure.json) · [Validation](artifacts/validation.json)
