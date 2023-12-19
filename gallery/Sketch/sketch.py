#!/usr/bin/env python

import hakowan as hkw
import lagrange
import math
import numpy as np
import pathlib


def draw(filename: pathlib.Path, config, rotate_angle):
    sketch = lagrange.SurfaceMesh()

    with open(filename, "r") as fin:
        for line in fin:
            if line.startswith("v "):
                fields = line.split()
                v = [float(x) for x in fields[1:]]
                sketch.add_vertex(v)
            elif line.startswith("l "):
                fields = line.split()
                l = np.array([int(x) - 1 for x in fields[1:]])
                sketch.add_polygon(l)

    base = (
        hkw.layer(sketch)
        .mark(hkw.mark.Curve)
        .channel(size=0.0005)
        .rotate([0, 1, 0], rotate_angle)
    )

    dark_line = base.channel(material=hkw.material.Plastic("#0C0609"))
    light_line = base.channel(material=hkw.material.Plastic("#CCCDD6"))

    stem = filename.stem
    dark_output_filename = pathlib.Path("results") / f"{stem}_dark.png"
    light_output_filename = pathlib.Path("results") / f"{stem}_light.png"

    hkw.render(dark_line, config, filename=dark_output_filename)
    hkw.render(light_line, config, filename=light_output_filename)


config = hkw.config()
config.z_up()
config.sensor.location = [1.5, -1.5, 1.5]
draw(pathlib.Path("data/Prof2task2_guitar_01_rough.obj"), config, 0)

config.y_up()
config.sensor.location = [1.75, 1.75, 1.75]
draw(pathlib.Path("data/designer2_guitar_01_rough.obj"), config, math.pi)
