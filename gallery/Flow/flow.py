#!/usr/bin/env python
import hakowan as hkw
import copy
import numpy as np

flow0 = hkw.layer("data/flow_00.ply")
flow2 = hkw.layer("data/flow_02.ply")
flow5 = hkw.layer("data/flow_05.ply")
flow9 = hkw.layer("data/flow_09.ply")

s = 0.3
mat = hkw.material.Principled(
    hkw.texture.ScalarField(
        hkw.attribute(
            "dist",
            scale=hkw.scale.Normalize(
                domain_min=-s, domain_max=s, range_min=0, range_max=1
            ),
        ),
    ),
    roughness=0.5,
    metallic=0.2,
)

dist0 = flow0.channel(material=copy.deepcopy(mat))
dist2 = flow2.channel(material=copy.deepcopy(mat))
dist5 = flow5.channel(material=copy.deepcopy(mat))
dist9 = flow9.channel(material=copy.deepcopy(mat))

config = hkw.config()
config.z_up()
config.sensor.location = [0, -2.5, 0]
config.film.width = 600
config.film.height = 1024

hkw.render(flow0, config, filename="results/bust_00.png")
hkw.render(flow2, config, filename="results/bust_02.png")
hkw.render(flow5, config, filename="results/bust_05.png")
hkw.render(flow9, config, filename="results/bust_09.png")

hkw.render(dist0, config, filename="results/bust_dist_00.png")
hkw.render(dist2, config, filename="results/bust_dist_02.png")
hkw.render(dist5, config, filename="results/bust_dist_05.png")
hkw.render(dist9, config, filename="results/bust_dist_09.png")
