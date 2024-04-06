#!/usr/bin/env python

import hakowan as hkw
import lagrange
import numpy as np

# Step 1: Preprocess data.

# The ref mesh contains the base geometry.
ref_mesh = lagrange.io.load_mesh("data/teaser_pig_bnb_target.obj")

# Chain mesh contains the layout boundaries.
# Each chain is a sequence of ref mesh vertices.
chains_mesh = lagrange.SurfaceMesh()
chains_mesh.add_vertices(ref_mesh.vertices)

# Load chains from the .lem file.
chains = []
with open("data/teaser_pig_bnb.lem", "r") as fin:
    for line in fin:
        if line.startswith("ee"):
            chain = line.split(":")[1].split()
            chain = [int(i) for i in chain]
            chains.append(chain)

# Add chains to the chain mesh.
for chain in chains:
    for i in range(len(chain) - 1):
        chains_mesh.add_polygon(np.array([chain[i], chain[i + 1]]))

# Compute layout charts.
involved_vertices = np.unique(np.hstack(chains)).tolist()
lagrange.compute_components(
    ref_mesh,
    output_attribute_name="chart",
    connectivity_type=lagrange.ConnectivityType.Vertex,
    blocker_elements=involved_vertices,
)

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
