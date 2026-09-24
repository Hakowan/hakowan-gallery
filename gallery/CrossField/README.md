# Cross-Field Streamlines

This example traces both orthogonal arms of a smooth four-fold rotationally symmetric (4-RoSy) field across a triangulated shark surface. The field is stored per facet, transported across mesh edges, and rendered as one-pixel screen-space curves over the surface.

[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/CrossField/results/shark_stream_lines.webp?raw=true"/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/CrossField/results/shark_stream_lines.webp?raw=true)

[Interactive demo](https://qnzhou.github.io/hakowan-gallery/gallery/CrossField/results/shark_stream_lines.html)

## Data

The cartoon shark model is designed by [Calrais](https://www.thingiverse.com/Calrais/designs) and published on [Thingiverse](https://www.thingiverse.com/thing:6306551).

It contains the triangular surface and the precomputed facet attribute `smooth_direction_field_facets` computed via the paper ["Globally Optimal Direction Fields"](https://www.cs.cmu.edu/~kmcrane/Projects/GloballyOptimalDirectionFields/).

## Input contract

- `mesh`: surface from `data/shark.msh`; `smooth_direction_field_facets` (facet 3-channel vector).

## Reproduce and inspect

```sh
python ../render_gallery.py --check CrossField
python ../render_gallery.py --artifacts CrossField
```

[Python](cross_field.py) · [Manifest](recipe.toml) · [Inspection](artifacts/inspect.json) · [Canonical JSON](artifacts/figure.json) · [Validation](artifacts/validation.json)
