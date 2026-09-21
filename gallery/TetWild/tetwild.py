#!/usr/bin/env python

import hakowan as hkw
from pathlib import Path

# Note that the `mtet` package used in `tet_utils` has not been released yet. Stay tuned!
from tet_utils import load_tet_mesh, extract_boundary, extract_clipped_boundary

hkw.set_default_backend("mitsuba")

# Create a clipping function for cut-away view of the tet mesh.
clip_coeff = [1, 1, 0.5, -30]


def cut_fn(c):
    return (
        c[0] * clip_coeff[0]
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

# Create surface and wire views of the data. These stay separate because the
# surface normal channel is invalid on curve marks.
surface = (
    hkw.layer()
    .name("Surface")
    .channel(normal="facet_normal")
    .material("Principled", "#FBCD50", roughness=0.2)
    .transform(hkw.transform.Compute(facet_normal="facet_normal"))
)
wires = (
    hkw.layer()
    .name("Edges")
    .mark("Curve")
    .channel(size=0.02)
    .material("Diffuse", "black")
)
bd_view = (surface + wires).data(bd_mesh)
surface = surface.material(
    "Principled",
    hkw.texture.ScalarField(
        "boundary_tag",
        colormap=["#FBCD50", "#0FB2F2"],
        categories=True,
        legend=hkw.Legend(title="Boundary type"),
    ),
    roughness=0.2,
)
clipped_view = (surface + wires).data(clipped_mesh)
combined_view = bd_view + clipped_view.translate([30, 0, 0])
clipped_view2 = hkw.layer(clipped_mesh2).material("ThinDielectric") + clipped_view

camera = hkw.PerspectiveCamera(eye=(0, -3, 0), up=(0, 0, 1))
environment = hkw.Environment(up=(0, 0, 1))
portrait_output = hkw.OutputSettings(width=800, height=1024)

for view, filename in (
    (bd_view, "results/bust_bd.webp"),
    (clipped_view, "results/bust_clipped.webp"),
    (clipped_view2, "results/bust_clipped2.webp"),
):
    figure = (
        hkw.figure(view).camera(camera).environment(environment).output(portrait_output)
    )
    hkw.render(figure, filename=filename)

combined_figure = (
    hkw.figure(combined_view)
    .camera(camera)
    .environment(environment)
    .output(width=1024, height=800)
)
RECIPE_FIGURE = combined_figure
RECIPE_INSPECTIONS = {"tetrahedral": bd_mesh}
RECIPE_DATA_IDS = {
    id(bd_mesh): "boundary",
    id(clipped_mesh): "clipped",
    id(clipped_mesh2): "clipped-inverse",
}
RECIPE_DATA_RESOLVER = {
    "boundary": bd_mesh,
    "clipped": clipped_mesh,
    "clipped-inverse": clipped_mesh2,
}
hkw.render(combined_figure, filename="results/bust.webp")
hkw.render(
    combined_figure,
    backend="webgl",
    filename="results/bust.html",
)
