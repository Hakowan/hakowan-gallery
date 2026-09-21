#!/usr/bin/env python

import hakowan as hkw
from data import load_data
import math

hkw.set_default_backend("mitsuba")

# Step 1: Preprocess data.
ref_mesh, chains_mesh = load_data()

# Step 2: Generate layout layers.
base = hkw.layer().rotate([0, 1, 0], -math.pi / 2)

# Mesh layer contains the base geometry.
# Use chart attribute as scalar field texture.
mesh_layer = (
    base.data(ref_mesh)
    .name("Surface charts")
    .material(
        "Principled",
        color=hkw.texture.ScalarField(
            "chart",
            colormap="set1",
            categories=True,
            legend=hkw.Legend(title="Chart"),
        ),
        roughness=0.0,
        metallic=0.0,
    )
)

# Chain layer contains the layout boundaries.
chains_layer = (
    base.data(chains_mesh)
    .name("Chart boundaries")
    .mark("Curve")
    .material("Conductor", "Cr")
    .channel(size=0.02)
)

scene = hkw.SceneSettings(camera=hkw.PerspectiveCamera(eye=(0, 0, 3)))

# Step 3: Render both layers.
solid_view = mesh_layer + chains_layer
RECIPE_FIGURE = hkw.Figure(solid_view, scene)
RECIPE_INSPECTIONS = {"surface": ref_mesh, "layout": chains_mesh}
RECIPE_DATA_IDS = {id(ref_mesh): "surface", id(chains_mesh): "layout"}
RECIPE_DATA_RESOLVER = {"surface": ref_mesh, "layout": chains_mesh}
hkw.render(RECIPE_FIGURE, filename="results/pig_embedded.webp")

# Step 4: Render the mesh layer with glass material.
transparent_view = mesh_layer.material("ThinDielectric") + chains_layer
hkw.render(
    hkw.Figure(transparent_view, scene),
    filename="results/pig_embedded_glass.webp",
)

# Step 5: Interactive demo
hkw.render(
    hkw.Figure(solid_view | transparent_view, scene),
    backend="webgl",
    filename="results/pig_embedded.html",
)
