#!/usr/bin/env python

import hakowan as hkw

hkw.set_default_backend("mitsuba")

base = hkw.layer("data/box.msh")
surface = (
    base.color_by("facet_id", categories=True, legend=False)
    .annotate(hkw.WorldAnnotation("Top", position=(0.0, 0.5, 0.0)))
    .annotate(hkw.WorldAnnotation("Bottom", position=(0.0, -0.5, 0.0)))
    .annotate(hkw.WorldAnnotation("Left", position=(-0.5, 0.0, 0.0)))
    .annotate(hkw.WorldAnnotation("Right", position=(0.5, 0.0, 0.0)))
    .annotate(hkw.WorldAnnotation("Front", position=(0.0, 0.0, 0.5)))
    .annotate(hkw.WorldAnnotation("Back", position=(0.0, 0.0, -0.5)))
    .name("Surface")
)
wireframe = (
    base.mark("Curve")
    .channel(
        size=hkw.channel.Size(data=0.005, space="scene"),
        material=hkw.material.Diffuse(reflectance="black"),
    )
    .name("Edges")
)

fig = (
    hkw.figure(surface + wireframe)
    .output(width=1024, height=800)
    .camera("orthographic", eye=(1, 1, 5))
)

RECIPE_FIGURE = fig
RECIPE_INSPECTIONS = {"mesh": "data/box.msh"}

hkw.render(fig, filename="results/box.webp")
hkw.render(fig, backend="webgl", filename="results/box.html")
