#!/usr/bin/env python

import hakowan as hkw

# Step 1: Create a base layer.
base = hkw.layer("data/bunny_heat.ply").channel(
    material=hkw.material.Principled(
        # We used isocontour texture to visualize the geodesic distance field both as color
        # and as isocurves.
        color=hkw.texture.Isocontour(
            data=hkw.attribute("dist", scale=100),
            texture1=hkw.texture.ScalarField(
                "dist",
                # Note that we used a custom colormap to approximate the original color map.
                colormap=["#F1D77E", "#A9150A", "black", "black", "black"],
            ),
            texture2="lightgray",
            ratio=0.95,
        ),
        roughness=0.5,
    )
)

# Step 2: Adjust camera position.
config = hkw.config()
config.sensor.location = [0, 1.2, 3]

# Step 3: Render the image.
hkw.render(base, config, filename="results/bunny_heat.png")
