#!/usr/bin/env python

import hakowan as hkw
import mitsuba as mi

# Step 1: Generate a base layer with normal and depth attributes.
base = hkw.layer("data/penny.glb").transform(
    hkw.transform.Compute(normal="normal", z="depth")
)
config = hkw.config()
config.sensor.location = [0, 0, 3]

# Step 2: Render with copper material.
l0 = base.material("RoughConductor", "Cu")
hkw.render(l0, config, filename="results/penny.png")

# Step 3: Update config setting for albedo-only rendering.
config.albedo_only = True

# Step 4: Render with normal AOV.
l1 = base.material("Principled", hkw.texture.ScalarField("normal", colormap="identity"))
hkw.render(l1, config, filename="results/penny_normal_aov.png")

# Step 5: Render with depth AOV.
l2 = base.material("Principled", hkw.texture.ScalarField("depth", colormap=[0, 1]))
hkw.render(l2, config, filename="results/penny_depth_aov.png")

# Step 6: Render with depth AOV using colormap.
l3 = base.material("Principled", color=hkw.texture.ScalarField("depth"))
hkw.render(l3, config, filename="results/penny_depth_aov_color.png")
