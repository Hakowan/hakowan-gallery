#!/usr/bin/env python
"""Render the four colored PCD flower scans in a 2×2 grid."""

import math
from pathlib import Path

import hakowan as hkw


ROOT = Path(__file__).resolve().parent
PCD_FILES = sorted((ROOT / "data").glob("*.pcd"))

# Lagrange's PCD loader decodes packed RGB into a uint8 vertex attribute.
vertex_color = hkw.texture.ScalarField(
    hkw.attribute("color", scale=1 / 255),
    colormap="identity",
    legend=False,
)
flowers = []
for path in PCD_FILES:
    flower = (
        hkw.layer(path)
        .name(path.stem.replace("_", " ").title())
        .mark("Point")
        .channel(size=hkw.channel.Size(data=5, space="screen"))
        .material("Principled", vertex_color, roughness=0.0, metallic=0.1)
        # View the scans from their acquisition side, with image Y pointing up.
        .rotate(axis=[1, 0, 0], angle=-math.pi / 2)
    )
    if "orchid" in path.stem:
        flower = flower.rotate(axis=[0, 1, 0], angle=-math.pi / 2)
    flowers.append(flower)

RECIPE_FIGURE = hkw.Figure(
    hkw.grid(flowers, columns=2, normalize=True, gap=0.15),
    hkw.SceneSettings(
        camera=hkw.OrthographicCamera(eye=(0, 0, 5), scale=2.2),
        output=hkw.OutputSettings(width=1200, height=1200),
    ),
)
RECIPE_INSPECTIONS = {path.stem: path for path in PCD_FILES}


if __name__ == "__main__":
    results = ROOT / "results"
    results.mkdir(exist_ok=True)
    hkw.render(RECIPE_FIGURE, backend="mitsuba", filename=results / "flowers.webp")
    hkw.render(RECIPE_FIGURE, backend="webgl", filename=results / "flowers.html")
