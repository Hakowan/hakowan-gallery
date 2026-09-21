#!/usr/bin/env python

import hakowan as hkw

hkw.set_default_backend("mitsuba")

base = (
    hkw.layer()
    .channel(normal="normal")
    .material(
        "Principled", "lightsteelblue", roughness=0.5, metallic=0.8, two_sided=True
    )
    .transform(hkw.transform.Compute(facet_normal="normal"))
)

l0 = base.data("data/mask_triangulated.obj").name("Initial")
l1 = base.data("data/mask_flow1.obj").name("Iteration 1")
l2 = base.data("data/mask_flow2.obj").name("Iteration 2")
l3 = base.data("data/mask_flow3.obj").name("Iteration 3")

static_camera = hkw.PerspectiveCamera(eye=(-1.5, 0.8, 2.5))
for layer, filename in (
    (l0, "results/mask_0.webp"),
    (l1, "results/mask_1.webp"),
    (l2, "results/mask_2.webp"),
    (l3, "results/mask_3.webp"),
):
    hkw.render(hkw.figure(layer).camera(static_camera), filename=filename)

# Interactive demo
interactive = hkw.figure(l0 | l1 | l2 | l3).camera("perspective", eye=(0, 0, 3))
RECIPE_FIGURE = interactive
RECIPE_INSPECTIONS = {"mesh": "data/mask_triangulated.obj"}
hkw.render(interactive, backend="webgl", filename="results/mask.html")
