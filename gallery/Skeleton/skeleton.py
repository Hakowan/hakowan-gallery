#!/usr/bin/env python

import hakowan as hkw
import lagrange
import numpy as np
import math

hkw.set_default_backend("mitsuba")

# Step 1: Load skeleton.
skeleton = lagrange.io.load_mesh("data/fertility_skeleton.obj")
with open("data/fertility_skeleton.obj", "r") as fin:
    for line in fin:
        if line.startswith("l "):
            fields = line.split()
            skeleton.add_polygon(np.array([int(fields[1]) - 1, int(fields[2]) - 1]))


# Step 2: Load base mesh with glass like material.
base = hkw.layer("data/fertility.obj").name("Surface").material("ThinDielectric")

skeleton_base = (
    hkw.layer(skeleton)
    .name("Skeleton joints")
    .material("Conductor", "Cr", two_sided=True)
)
skeleton_edges = skeleton_base.name("Skeleton edges").mark("Curve").channel(size=0.01)

# Step 3: Combine all layers
all_layers = (base + skeleton_base + skeleton_edges).rotate(
    axis=[0, 1, 0], angle=math.pi / 6
)

RECIPE_FIGURE = hkw.figure(all_layers).camera("perspective", eye=(0, 0, 3))
RECIPE_INSPECTIONS = {
    "surface": "data/fertility.obj",
    "skeleton": skeleton,
}
RECIPE_DATA_IDS = {id(skeleton): "skeleton"}
RECIPE_DATA_RESOLVER = {"skeleton": skeleton}

# Step 4: Add the renderer-specific volume integrator to the declared scene.
config = RECIPE_FIGURE.to_config()
config.integrator = hkw.setup.integrator.VolPath()
hkw.render(
    RECIPE_FIGURE,
    config,
    filename="results/fertility_skeleton.webp",
)

# Step 5: Interactive demo
hkw.render(
    RECIPE_FIGURE,
    config,
    backend="webgl",
    filename="results/fertility_skeleton.html",
)
