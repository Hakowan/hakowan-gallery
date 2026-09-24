#!/usr/bin/env python

import hakowan as hkw
from curve_io import load_curves
import lagrange
from pathlib import Path

hkw.set_default_backend("mitsuba")

# Step 1: Laod in the fibrers
fibers = load_curves(Path("data/fibers.obj"))
fiber_ids = fibers.attribute("curve_id").data
fiber_set = lagrange.separate_by_facet_groups(fibers, fiber_ids)

# Step 2: Create a layer for each fiber with different color.
num_fibers = len(fiber_set)
root_layer = hkw.layer()
colormap = hkw.common.colormap.named_colormaps.paired
for i, fiber in enumerate(fiber_set):
    c = colormap(i / (num_fibers - 1)).data.tolist()
    fiber_layer = (
        hkw.layer(fiber).mark("Curve").channel(size=0.3).material("Plastic", c)
    )
    root_layer.children.append(fiber_layer)

scene = hkw.SceneSettings(camera=hkw.PerspectiveCamera(eye=(0, 0, 3)))
RECIPE_FIGURE = hkw.Figure(root_layer, scene)
RECIPE_INSPECTIONS = {"fibers": fibers}
RECIPE_DATA_IDS = {id(fiber): f"fiber-{index}" for index, fiber in enumerate(fiber_set)}
RECIPE_DATA_RESOLVER = {
    f"fiber-{index}": fiber for index, fiber in enumerate(fiber_set)
}

# Step 3: Render
hkw.render(RECIPE_FIGURE, filename="results/fibers.webp")
hkw.render(RECIPE_FIGURE, backend="webgl", filename="results/fibers.html")
