#!/usr/bin/env python

import hakowan as hkw
from curve_io import load_curves
import lagrange
from pathlib import Path

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
    l = (
        hkw.layer(fiber)
        .mark(hkw.mark.Curve)
        .channel(size=0.3, material=hkw.material.Plastic(c))
    )
    root_layer.children.append(l)

# Step 3: Render
config = hkw.config()
config.sensor.location = [0, 0, 3]
hkw.render(root_layer, config, filename="results/fibers.png")
