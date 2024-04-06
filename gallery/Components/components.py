#!/usr/bin/env python

import hakowan as hkw
import math

base = hkw.layer("data/foot.ply")
base = base.material(
    "Principled",
    color=hkw.texture.ScalarField("comp", colormap="set1", categories=True),
    roughness=0.2,
).transform(hkw.transform.Compute(component="comp"))

front_view = base.rotate(axis=[0, 1, 0], angle=math.pi)
top_view = base.rotate(axis=[1, 0, 0], angle=math.pi / 2)
side_view = base.rotate(axis=[0, 1, 0], angle=math.pi / 2)

config = hkw.config()
config.sensor.location = [0, 0, 3.5]

hkw.render(front_view, config, filename="results/foot_front.png")
hkw.render(top_view, config, filename="results/foot_top.png")
hkw.render(side_view, config, filename="results/foot_side.png")
