#!/usr/bin/env python

import hakowan as hkw

base = (
    hkw.layer("data/icosahedron.ply")
    .mark("Point")
    .material("Plastic", "ivory")
    .channel(size=0.045)
    .transform(hkw.transform.Compute(vertex_normal="normal"))
)

spheres = base.channel(shape=hkw.channel.Shape("sphere", orientation="normal"))
boxes = base.channel(shape=hkw.channel.Shape("cube", orientation="normal"))
disks = base.channel(shape=hkw.channel.Shape("disk", orientation="normal"))

fig = hkw.Figure(hkw.grid([spheres, boxes, disks], rows=1, gap=0.5)).camera(
    eye=[0, 0, 3]
)

RECIPE_FIGURE = fig
RECIPE_INSPECTIONS = {"icosphere": "data/icosahedron.ply"}

if __name__ == "__main__":
    hkw.render(RECIPE_FIGURE, backend="webgl", filename="results/points.html")
    hkw.render(RECIPE_FIGURE, backend="mitsuba", filename="results/points.webp")
