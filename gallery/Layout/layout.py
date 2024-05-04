#!/usr/bin/env python

import hakowan as hkw
from data import load_data

# Step 1: Preprocess data.
ref_mesh, chains_mesh = load_data()

# Step 2: Generate layout layers.
base = hkw.layer(ref_mesh)

# Mesh layer contains the base geometry.
# Use chart attribute as scalar field texture.
mesh_layer = base.material(
    "Principled",
    color=hkw.texture.ScalarField("chart", colormap="set1", categories=True),
    roughness=0.0,
    metallic=0.0,
)

# Chain layer contains the layout boundaries.
chains_layer = (
    hkw.layer(chains_mesh)
    .mark("Curve")
    .material("Conductor", "Cr")
    .channel(size=0.02)
)

# Update camera location for better viewing angle.
config = hkw.config()
config.sensor.location = [3, 0, 0]

# Step 3: Render the both layers.
hkw.render(mesh_layer + chains_layer, config, filename="results/pig_embedded.png")

# Step 4: Render the mesh layer with glass material.
mesh_layer = base.channel(material=hkw.material.ThinDielectric())
hkw.render(mesh_layer + chains_layer, config, filename="results/pig_embedded_glass.png")
