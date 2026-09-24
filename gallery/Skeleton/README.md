# Neural Skeleton

This example tries to reproduce skeleton visualization from the paper "[Neural
skeleton: Implicit neural representation away from the
surface](https://hal.science/hal-04159959v1/document)".

[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Skeleton/results/fertility_skeleton.webp?raw=true"/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Skeleton/results/fertility_skeleton.webp?raw=true)

[Interactive
demo](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Skeleton/results/fertility_skeleton.html)

## Data

The skeleton is computed with the [official
code](https://github.com/MClemot/SkeletonLearning) released by the authors.

## Input contract

- `surface`: surface from `data/fertility.obj`; no pre-existing attributes required.
- `skeleton`: curve from `data/fertility_skeleton.obj`; no pre-existing attributes required.

## Reproduce and inspect

```sh
python ../render_gallery.py --check Skeleton
python ../render_gallery.py --artifacts Skeleton
```

[Python](skeleton.py) · [Manifest](recipe.toml) · [Inspection](artifacts/inspect.json) · [Canonical JSON](artifacts/figure.json) · [Validation](artifacts/validation.json)
