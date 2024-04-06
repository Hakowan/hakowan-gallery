#!/usr/bin/env python3

import hakowan as hkw
import pathlib
import math

# Generate base layer setting.
# We are using image-based texture for color in this example.
# The UV is scaled by 10 times for visualizaiton purposes.
base = hkw.layer().material(
    "Principled",
    color=hkw.texture.Image(
        filename=pathlib.Path("data/texture.png"),
        uv=hkw.attribute("texcoord", scale=10),
    ),
    roughness=0.2,
)

# Figure 3
fig3 = base.data("data/fig3.obj").rotate(axis=[0, 1, 0], angle=math.pi)

# Move the camera position closer.
config = hkw.config()
config.sensor.location = [0, 0, 3]

# Render!
#hkw.render(fig3, config, filename="results/fig3.png")

# Figure 10

# The input mesh comes at an odd orientation.
# We apply two rotations to fix the orientation issue.
# First, we rotate the mesh around the x-axis by -45 degrees.
# Then, we rotate the mesh around the y-axis by 135 degrees.
fig10 = (
    base.data("data/fig10_uniform.obj")
    .rotate(axis=[1, 0, 0], angle=-math.pi / 4)
    .rotate(axis=[0, 1, 0], angle=3 * math.pi / 4)
)

# Render!
hkw.render(fig10, config, filename="results/fig10.png")
