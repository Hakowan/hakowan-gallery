#!/usr/bin/env python

import hakowan as hkw
import math

hkw.set_default_backend("mitsuba")

# Step 1: Create a base layer.
base = hkw.layer("data/bunny_heat.ply").material(
    "Principled",
    # We used isocontour texture to visualize the geodesic distance field both as color
    # and as isocurves.
    color=hkw.texture.Isocontour(
        data="dist",
        texture1=hkw.texture.ScalarField(
            "dist",
            colormap="fire",
            reverse=True,
            domain=(0, 0.12),
            legend=hkw.Legend(title="Geodesic distance"),
        ),
        texture2=hkw.texture.ScalarField(
            "dist",
            colormap=["white", "lightgray"],
            domain=(0, 0.12),
            legend=False,
        ),
        ratio=0.90,
        num_contours=100,
    ),
    roughness=0.5,
)

# Step 2: Declare the shared camera once for every output.
scene = hkw.SceneSettings(
    camera=hkw.PerspectiveCamera(eye=(0, 1.2, 3)),
)
RECIPE_FIGURE = hkw.Figure(base, scene)
RECIPE_INSPECTIONS = {"mesh": "data/bunny_heat.ply"}

# Step 3: Render the image.
hkw.render(RECIPE_FIGURE, filename="results/bunny_heat.webp")

# Step 4: Render the back side.
back_side = base.rotate(axis=[0, 1, 0], angle=math.pi)
hkw.render(hkw.Figure(back_side, scene), filename="results/bunny_heat_back.webp")

# Step 5: Interactive demo
hkw.render(RECIPE_FIGURE, backend="webgl", filename="results/bunny_heat.html")
