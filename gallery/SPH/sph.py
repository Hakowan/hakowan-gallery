#!/usr/bin/env python

import hakowan as hkw
import lagrange
import numpy as np

emitter = hkw.layer("data/emitter.msh").channel(
    material=hkw.material.RoughPlastic("Ivory")
)

box_min = [-1.223, -0.5, -1.226]
box_max = [1.224, 4.0, 1.222]
roi_box = np.vstack([box_min, box_max])
for i in [10, 30, 60, 133]:
    fluid = (
        (
            hkw.layer()
            .data(f"data/waterbell_{i:03}.msh", roi_box=roi_box)
            .mark(hkw.mark.Point)
            .channel(
                material=hkw.material.Principled(
                    hkw.texture.ScalarField(
                        hkw.attribute("speed", scale=hkw.scale.Clip([0, 10]))
                    )
                ),
                size=0.01,
            )
        )
        .transform(hkw.transform.Norm("velocity", "speed"))
        .transform(hkw.transform.Filter(data=None, condition=lambda p: p[2] <= 0))
    )
    config = hkw.config()
    config.sensor.location = [0, 0, 3]
    hkw.render(fluid + emitter, config, filename=f"results/waterbell_{i:03}.png")
