#!/usr/bin/env python

import hakowan as hkw
import lagrange
import numpy as np
import math

# Step 1: Load skeleton.
skeleton = lagrange.io.load_mesh("data/fertility_skeleton.obj")
with open("data/fertility_skeleton.obj", "r") as fin:
    for line in fin:
        if line.startswith("l "):
            fields = line.split()
            skeleton.add_polygon(np.array([int(fields[1]) - 1, int(fields[2]) - 1]))


# Step 2: Load base mesh with glass like material.
base = hkw.layer("data/fertility.obj").material("ThinDielectric")

skeleton_base = hkw.layer(skeleton).material("Conductor", "Cr")
skeleton_edges = skeleton_base.mark("Curve").channel(size=0.01)

# Step 3: Combine all layers
all_layers = (base + skeleton_base + skeleton_edges).rotate(
    axis=[0, 1, 0], angle=math.pi / 6
)

# Step 4: Adjust camera and render.
config = hkw.config()
config.sensor.location = [0, 0, 3]
config.integrator = hkw.setup.integrator.VolPath()
hkw.render(
    all_layers,
    config,
    filename="results/fertility_skeleton.png",
)
