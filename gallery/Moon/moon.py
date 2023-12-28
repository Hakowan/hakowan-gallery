#!/usr/bin/env python

import hakowan as hkw
import pathlib

config = hkw.config()
config.z_up()
config.emitters[0].rotation = -90
config.sensor.location = [3, 0, 0]

# Render with both color and bump map.
base = hkw.layer("data/moon.ply").channel(
    material=hkw.material.Principled(
        color=hkw.texture.Image(pathlib.Path("data/lroc_color_poles_8k.png")),
        bump_map=hkw.texture.Image(pathlib.Path("data/ldem_16_uint.png")),
        bump_scale=0.1,
    )
)
hkw.render(base, config, filename="results/moon.png")

# Render back side.
config.emitters[0].rotation = 90
config.sensor.location = [-3, 0, 0]
base = hkw.layer("data/moon.ply").channel(
    material=hkw.material.Principled(
        color=hkw.texture.Image(pathlib.Path("data/lroc_color_poles_8k.png")),
        bump_map=hkw.texture.Image(pathlib.Path("data/ldem_16_uint.png")),
        bump_scale=0.1,
    )
)
hkw.render(base, config, filename="results/moon_backside.png")
