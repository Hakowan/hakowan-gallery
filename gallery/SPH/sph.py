#!/usr/bin/env python

import hakowan as hkw
import lagrange
import numpy as np

config = hkw.config()
config.sensor.location = [0, 0, 3]

emitter = hkw.layer("data/emitter.msh").channel(
    material=hkw.material.RoughPlastic("Ivory")
)

box_min = [-1.223, -0.5, -1.226]
box_max = [1.224, 4.0, 1.222]
roi_box = np.vstack([box_min, box_max])
for i in [10, 30, 60, 133]:
    fluid = (
        hkw.layer()
        .data(f"data/waterbell_{i:03}.msh", roi_box=roi_box)
        .mark("Point")
        .channel(size=0.01)
        .material(
            "Principled",
            hkw.texture.ScalarField("speed", domain=[0, 10]),
        )
    ).transform(hkw.transform.Norm("velocity", "speed"))
    hkw.render(fluid + emitter, config, filename=f"results/waterbell_{i:03}_all.png")

    fluid = fluid.transform(hkw.transform.Filter(condition=lambda p: p[2] <= 0))
    hkw.render(fluid + emitter, config, filename=f"results/waterbell_{i:03}.png")
