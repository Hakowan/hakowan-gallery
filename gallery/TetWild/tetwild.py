#!/usr/bin/env python

import hakowan as hkw
import numpy as np
import lagrange
from pathlib import Path

# Note that the `mtet` package used in `tet_utils` has not been released yet. Stay tuned!
from tet_utils import load_tet_mesh, extract_boundary, extract_clipped_boundary

# Create a clipping function for cut-away view of the tet mesh.
clip_coeff = [1, 1, 0.5, -30]
cut_fn = (
    lambda c: c[0] * clip_coeff[0]
    + c[1] * clip_coeff[1]
    + c[2] * clip_coeff[2]
    + clip_coeff[3]
    > 0
)

# Extract the tet mesh data.
tet_mesh = load_tet_mesh(Path("data/bust.msh"))
bd_mesh = extract_boundary(tet_mesh)
clipped_mesh = extract_clipped_boundary(tet_mesh, cut_fn)
clipped_mesh2 = extract_clipped_boundary(tet_mesh, lambda p: not cut_fn(p))

# Create a surface and wire view of the data.
surface = (
    hkw.layer()
    .channel(normal="facet_normal")
    .material("Principled", "#FBCD50", roughness=0.2)
    .transform(hkw.transform.Compute(facet_normal="facet_normal"))
)
wires = hkw.layer().mark("Curve").channel(size=0.02).material("Diffuse", "black")

# Create boundary and clipped views.
bd_view = (surface + wires).data(bd_mesh)
surface = surface.material(
    "Principled",
    hkw.texture.ScalarField("boundary_tag", colormap=["#FBCD50", "#0FB2F2"]),
    roughness=0.2,
)
clipped_view = (surface + wires).data(clipped_mesh)
combined_view = bd_view + clipped_view.translate([30, 0, 0])
clipped_view2 = hkw.layer(clipped_mesh2).material("ThinDielectric") + clipped_view

# Render the views.
config = hkw.config()
config.z_up()
config.sensor.location = [0, -3, 0]
config.film.width = 800
config.film.height = 1024
hkw.render(bd_view, config, filename="results/bust_bd.png")
hkw.render(clipped_view, config, filename="results/bust_clipped.png")
hkw.render(clipped_view2, config, filename="results/bust_clipped2.png")

config.film.width = 1024
config.film.height = 800
config.sensor.location = [0, -3, 0]
hkw.render(combined_view, config, filename="results/bust.png")
