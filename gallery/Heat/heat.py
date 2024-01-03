#!/usr/bin/env python

import hakowan as hkw
import math

# Step 1: Create a base layer.
base = hkw.layer("data/bunny_heat.ply").channel(
    material=hkw.material.Principled(
        # We used isocontour texture to visualize the geodesic distance field both as color
        # and as isocurves.
        color=hkw.texture.Isocontour(
            data="dist",
            texture1=hkw.texture.ScalarField(
                "dist",
                # Note that we used a custom colormap to approximate the original color map.
                colormap=["#a69c65", "#9A9A07", "#983A06", "#7C070A", "#160507", "#060103", "#000000"],
            ),
            texture2="lightgray",
            ratio=0.95,
            num_contours=100,
        ),
        roughness=0.5,
    )
)

# Step 2: Adjust camera position.
config = hkw.config()
config.sensor.location = [0, 1.2, 3]

# Step 3: Render the image.
hkw.render(base, config, filename="results/bunny_heat.png")

# Step 4: Render the back side.
back_side = base.rotate(axis=[0, 1, 0], angle=math.pi)
hkw.render(back_side, config, filename="results/bunny_heat_back.png")
