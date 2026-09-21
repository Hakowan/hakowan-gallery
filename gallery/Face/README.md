# Face UV

This example visualizes the UV coordinates of a face model in two ways. The first way uses
checkerboard texture to visualize UV. The second way visualize the UV mesh with the 3D normal field.

[<img width=25% src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Face/results/face.webp?raw=true"/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Face/results/face.webp?raw=true)
[<img width=25% src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Face/results/face_checkerboard.webp?raw=true"/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Face/results/face_checkerboard.webp?raw=true)
[<img width=40% src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Face/results/face_uv.webp?raw=true"/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Face/results/face_uv.webp?raw=true)

[Interactive demo](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/Face/results/face_all.html)

## Data

The face mesh is the [connonical face model](https://github.com/google/mediapipe/blob/v0.10.9/mediapipe/modules/face_geometry/data/canonical_face_model.obj) released by Google as part of the [MediaPipe project](https://github.com/google/mediapipe) (Apache-2.0 license).

## Input contract

- `mesh`: surface from `data/canonical_face_model.obj`; no pre-existing attributes required.

## Reproduce and inspect

```sh
python ../render_gallery.py --check Face
python ../render_gallery.py --artifacts Face
```

[Python](face.py) · [Manifest](recipe.toml) · [Inspection](artifacts/inspect.json) · [Canonical JSON](artifacts/figure.json) · [Validation](artifacts/validation.json)
