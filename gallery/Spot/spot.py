#!/usr/bin/env python

import hakowan as hkw

hkw.set_default_backend("mitsuba")

base = hkw.layer("data/spot_quadrangulated.obj")
view = (
    base.name("Surface")
    .mark("Surface")
    .material("Principled", "ivory", roughness=0.35)
    .show_edges(color="#202020", width=0.002, name="Wireframe")
)

figure = (
    hkw.figure(view)
    .camera("perspective", eye=(3.5, 0, 0), up=(0, 1, 0))
    .environment(up=(0, 1, 0))
)
RECIPE_FIGURE = figure
RECIPE_INSPECTIONS = {"mesh": "data/spot_quadrangulated.obj"}

hkw.render(figure, filename="results/spot_wireframe.webp")
hkw.render(figure, backend="webgl", filename="results/spot_wireframe.html")
