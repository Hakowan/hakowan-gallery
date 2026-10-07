# Flowers

This example renders four scanned flower point clouds with their captured RGB colors in a normalized 2×2 grid. Screen-space point marks and an orthographic camera show the scans from their acquisition side; the orchid receives an additional rotation.

[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Flowers/results/flowers.webp?raw=true"/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Flowers/results/flowers.webp?raw=true)

[Interactive demo](https://qnzhou.github.io/hakowan-gallery/gallery/Flowers/results/flowers.html)

## Data

The data is from the [4D Reconstruction of Blooming Flowers project](https://vcc.tech/research/2017/Flowers) (Computer Graphics Forum, 2017). The bundled scans are [`golden_lily_130.pcd`](data/golden_lily_130.pcd), [`lily_127.pcd`](data/lily_127.pcd), [`orchid_113.pcd`](data/orchid_113.pcd), and [`water_lily_72.pcd`](data/water_lily_72.pcd).

The project's data and code are free for **research and education use only**. The authors require citing their paper when using any part of their algorithm, code, data, or results in a publication:

> Qian Zheng, Xiaochen Fan, Minglun Gong, Andrei Sharf, Oliver Deussen, and Hui Huang. “4D Reconstruction of Blooming Flowers.” *Computer Graphics Forum* 36(6), 405–417, 2017.

The PCD loader decodes packed RGB into a three-channel `uint8` vertex attribute named `color`. The renderer scales it from 0–255 to 0–1 and uses the identity colormap without a legend. No preprocessing is required.

## Render

With Hakowan and its Mitsuba and WebGL backends installed, run from this directory:

```sh
python flowers.py
```

This writes the 1200×1200 static image to `results/flowers.webp` and the interactive viewer to `results/flowers.html`.

## Input contract

- `golden_lily_130`: point-cloud from `data/golden_lily_130.pcd`; `color` (vertex 3-channel color).
- `lily_127`: point-cloud from `data/lily_127.pcd`; `color` (vertex 3-channel color).
- `orchid_113`: point-cloud from `data/orchid_113.pcd`; `color` (vertex 3-channel color).
- `water_lily_72`: point-cloud from `data/water_lily_72.pcd`; `color` (vertex 3-channel color).

## Reproduce and inspect

```sh
python ../render_gallery.py --check Flowers
python ../render_gallery.py --artifacts Flowers
```

[Python](flowers.py) · [Manifest](recipe.toml) · [Inspection](artifacts/inspect.json) · [Canonical JSON](artifacts/figure.json) · [Validation](artifacts/validation.json)
