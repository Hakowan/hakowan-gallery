#!/usr/bin/env python

import hakowan as hkw
from image2mesh import image2mesh

# Step 1: Generate a mesh from a heightmap.
usgs_data = image2mesh("data/USGS_1_n35w112.tif")

# Step 2: Create a map layer that maps elevation to color.
# Note that we use a custom colormap here.
usgs_map = (
    hkw.layer(usgs_data)
    .channel(
        material=hkw.material.Principled(
            color=hkw.texture.ScalarField(
                "elevation", colormap=["#15A887", "#8C4E37", "#E9ECF2"]
            )
        )
    )
    .transform(hkw.transform.Compute(z="elevation"))
)

# Step 3: Render from two different angles.
config = hkw.config()
config.sensor.location = [0, 0, 3]
hkw.render(usgs_map, config, filename="results/usgs_1_n35112.png")

config.sensor.location = [0, -2, 2]
hkw.render(usgs_map, config, filename="results/usgs_1_n35112_side.png")
