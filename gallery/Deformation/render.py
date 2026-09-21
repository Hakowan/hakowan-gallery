#!/usr/bin/env python

import hakowan as hkw
from hakowan.spec import compile_expression

hkw.set_default_backend("mitsuba")

# Handle layer with rough plastic material.
handles = (
    hkw.layer()
    .name("Handles")
    .material("RoughPlastic", "steelblue")
    .transform(
        hkw.transform.Filter(
            data="label", condition=compile_expression("value in (1, 2)")
        )
    )
)

# Deformed region with smooth conductor material.
deformed_region = (
    hkw.layer()
    .name("Deformed region")
    .material("Conductor", "Hg")
    .isolate_component(0, attribute="label", compute=False)
)

# Create four different layers with different inptu data.
l1 = (handles + deformed_region).data("data/cylinder_1.msh")
l2 = (handles + deformed_region).data("data/cylinder_2.msh")
l3 = (handles + deformed_region).data("data/cylinder_3.msh")
l4 = (handles + deformed_region).data("data/cylinder_4.msh")

# Reuse one declarative scene across the four simulation states.
scene = hkw.SceneSettings(
    camera=hkw.PerspectiveCamera(eye=(0, -3, 0), up=(0, 0, 1)),
    environment=hkw.Environment(up=(0, 0, 1)),
)
RECIPE_FIGURE = hkw.Figure(l1 | l2 | l3 | l4, scene)
RECIPE_INSPECTIONS = {"mesh": "data/cylinder_1.msh"}

for index, layer in enumerate((l1, l2, l3, l4), start=1):
    hkw.render(hkw.Figure(layer, scene), filename=f"results/cylinder_{index}.webp")

# Interactive comparison.
hkw.render(RECIPE_FIGURE, backend="webgl", filename="results/cylinders.html")
