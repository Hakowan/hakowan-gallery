#!/usr/bin/env python

import hakowan as hkw

hkw.set_default_backend("mitsuba")

base = hkw.layer("data/powell_sabin.ply").transform(
    hkw.transform.Compute(component="comp_ids", facet_normal="face_normal")
)

vertices = (
    base.name("Vertices")
    .mark("Point")
    .channel(size=0.015)
    .material(
        "Principled",
        hkw.texture.ScalarField(
            "vertex_label",
            colormap=["steelblue", "green", "yellow", "red"],
            categories=True,
            legend=hkw.Legend(title="Vertex type"),
        ),
        roughness=0,
        metallic=0.3,
    )
)
edges = base.name("Edges").mark("Curve").material("Conductor", "Cr").channel(size=0.005)
surface = (
    base.name("Surface")
    .mark("Surface")
    .material(
        "Principled",
        color=hkw.texture.ScalarField(
            "comp_ids",
            colormap="set1",
            categories=True,
            legend=hkw.Legend(title="Component"),
        ),
    )
)

scene = hkw.SceneSettings(
    camera=hkw.PerspectiveCamera(eye=(2.5, -2.5, 0), up=(0, 0, 1)),
    environment=hkw.Environment(up=(0, 0, 1)),
)
regular_view = vertices + edges + surface
RECIPE_FIGURE = hkw.Figure(regular_view, scene)
RECIPE_INSPECTIONS = {"mesh": "data/powell_sabin.ply"}
hkw.render(RECIPE_FIGURE, filename="results/powell_sabin.webp")

exploded_view = regular_view.transform(hkw.transform.Explode("comp_ids", magnitude=0.5))
hkw.render(
    hkw.Figure(exploded_view, scene),
    filename="results/powell_sabin_explode.webp",
)

hkw.render(
    hkw.Figure(regular_view | exploded_view, scene),
    backend="webgl",
    filename="results/powell_sabin.html",
)
