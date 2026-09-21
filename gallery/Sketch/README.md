# Lifting Freehand Concept Sketches into 3D

This example aims to visualize the 3D freehand sketches generated from the paper "[Lifting Freehand
Concept Sketches into 3D](https://ns.inria.fr/d3/Lift3D/)".

[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Sketch/results/designer2_guitar_01_rough_light.webp?raw=true#only-dark" width=45%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Sketch/results/designer2_guitar_01_rough_light.webp?raw=true)
[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Sketch/results/Prof2task2_guitar_01_rough_light.webp?raw=true#only-dark" width=45%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Sketch/results/Prof2task2_guitar_01_rough_light.webp?raw=true)
[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Sketch/results/designer2_guitar_01_rough_dark.webp?raw=true#only-light" width=45%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Sketch/results/designer2_guitar_01_rough_dark.webp?raw=true)
[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Sketch/results/Prof2task2_guitar_01_rough_dark.webp?raw=true#only-light" width=45%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Sketch/results/Prof2task2_guitar_01_rough_dark.webp?raw=true)

[Interactive demos: professor sketch](https://qnzhou.github.io/hakowan-gallery/gallery/Sketch/results/Prof2task2_guitar_01_rough.html) · [designer sketch](https://qnzhou.github.io/hakowan-gallery/gallery/Sketch/results/designer2_guitar_01_rough.html)

## Data

The data used for this example comes from the officially released [reconstruction
results](https://repo-sam.inria.fr/d3/Lift3D/reconstructions.zip).

## Input contract

- `sketch`: curve from `data/Prof2task2_guitar_01_rough.obj`; no pre-existing attributes required.

## Reproduce and inspect

```sh
python ../render_gallery.py --check Sketch
python ../render_gallery.py --artifacts Sketch
```

[Python](sketch.py) · [Manifest](recipe.toml) · [Inspection](artifacts/inspect.json) · [Canonical JSON](artifacts/figure.json) · [Validation](artifacts/validation.json)
