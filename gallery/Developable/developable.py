#!/usr/bin/env python

import hakowan as hkw

base = (
    hkw.layer()
    .channel(normal="normal")
    .material(
        "Principled", "lightsteelblue", roughness=0.5, metallic=0.8, two_sided=True
    )
    .transform(hkw.transform.Compute(facet_normal="normal"))
)

l0 = base.data("data/mask_triangulated.obj")
l1 = base.data("data/mask_flow1.obj")
l2 = base.data("data/mask_flow2.obj")
l3 = base.data("data/mask_flow3.obj")

config = hkw.config()
config.sensor.location = [-1.5, 0.8, 2.5]

hkw.render(l0, config, filename="results/mask_0.png")
hkw.render(l1, config, filename="results/mask_1.png")
hkw.render(l2, config, filename="results/mask_2.png")
hkw.render(l3, config, filename="results/mask_3.png")
