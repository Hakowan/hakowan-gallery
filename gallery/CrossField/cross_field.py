#!/usr/bin/env python

import hakowan as hkw
import numpy as np

hkw.set_default_backend("mitsuba")

base = hkw.layer("data/shark.msh").rotate((0, 0, 1), np.radians(90))
surface = base.name("Surface")
stream_lines = (
    base.transform(
        hkw.transform.Streamline(
            vec_field="smooth_direction_field_facets",
            cross_field=True,
            n=500,
            max_steps=100,
        )
    )
    .name("Wireframe")
    .mark("Curve")
    .channel(size=hkw.channel.Size(data=1, space="screen"))
    .material("Diffuse", "#202020")
)


figure = (
    hkw.figure(surface + stream_lines)
    .camera("perspective", eye=(0, -3, 0), up=(0, 0, 1))
    .environment(up=(0, 0, 1))
)
RECIPE_FIGURE = figure
RECIPE_INSPECTIONS = {"mesh": "data/shark.msh"}

if __name__ == "__main__":
    hkw.render(figure, filename="results/shark_stream_lines.webp")
    hkw.render(figure, backend="webgl", filename="results/shark_stream_lines.html")
