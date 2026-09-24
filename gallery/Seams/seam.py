#!/usr/bin/env python

import hakowan as hkw

hkw.set_default_backend("mitsuba")

base = hkw.layer("data/spot_quadrangulated.obj")
surface_view = base.name("Surface")
seam_view = (
    base.transform(hkw.transform.Boundary(attributes=["texcoord"]))
    .name("Seam")
    .mark("Curve")
    .material("Diffuse", "black")
    .channel(size=hkw.channel.Size(data=1, space="screen"))
)

figure = (
    hkw.figure(surface_view + seam_view)
    .camera("perspective", eye=(3.5, 0, 0), up=(0, 1, 0))
    .environment(up=(0, 1, 0))
)

RECIPE_FIGURE = figure
RECIPE_INSPECTIONS = {"mesh": "data/spot_quadrangulated.obj"}

hkw.render(figure, filename="results/spot_seam.webp")
hkw.render(figure, backend="webgl", filename="results/spot_seam.html")
