#!/usr/bin/env python

import hakowan as hkw
import lagrange
import math
import numpy as np
import pathlib

hkw.set_default_backend("mitsuba")


def draw(filename: pathlib.Path, rotate_angle, *, eye, up):
    sketch = lagrange.SurfaceMesh()

    with open(filename, "r") as fin:
        for line in fin:
            if line.startswith("v "):
                fields = line.split()
                v = [float(x) for x in fields[1:]]
                sketch.add_vertex(v)
            elif line.startswith("l "):
                fields = line.split()
                indices = np.array([int(x) - 1 for x in fields[1:]])
                sketch.add_polygon(indices)

    base = (
        hkw.layer(sketch)
        .mark(hkw.mark.Curve)
        .channel(size=0.0005)
        .rotate([0, 1, 0], rotate_angle)
    )

    dark_line = base.channel(material=hkw.material.Plastic("#0C0609"))
    light_line = base.channel(material=hkw.material.Plastic("#CCCDD6"))

    stem = filename.stem
    dark_output_filename = pathlib.Path("results") / f"{stem}_dark.webp"
    light_output_filename = pathlib.Path("results") / f"{stem}_light.webp"

    for layer, out in [
        (dark_line, dark_output_filename),
        (light_line, light_output_filename),
    ]:
        figure = (
            hkw.figure(layer).camera("perspective", eye=eye, up=up).environment(up=up)
        )
        hkw.render(figure, filename=out)

    interactive = (
        hkw.figure(dark_line).camera("perspective", eye=eye, up=up).environment(up=up)
    )
    hkw.render(
        interactive,
        backend="webgl",
        filename=pathlib.Path("results") / f"{stem}.html",
    )
    return interactive, sketch


RECIPE_FIGURE, _recipe_sketch = draw(
    pathlib.Path("data/Prof2task2_guitar_01_rough.obj"),
    0,
    eye=(1.5, -1.5, 1.5),
    up=(0, 0, 1),
)
RECIPE_INSPECTIONS = {"sketch": _recipe_sketch}
RECIPE_DATA_IDS = {id(_recipe_sketch): "sketch"}
RECIPE_DATA_RESOLVER = {"sketch": _recipe_sketch}

draw(
    pathlib.Path("data/designer2_guitar_01_rough.obj"),
    math.pi,
    eye=(1.75, 1.75, 1.75),
    up=(0, 1, 0),
)
