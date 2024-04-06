#!/usr/bin/env python

import hakowan as hkw
import pathlib

config = hkw.config()
config.z_up()
config.emitters[0].rotation = -90
config.sensor.location = [3, 0, 0]

# Render with both color and bump map.
base = (
    hkw.layer("data/moon.ply")
    .channel(
        bump_map=hkw.channel.BumpMap(
            hkw.texture.Image("data/ldem_16_uint.png"), scale=0.1
        ),
    )
    .material("Principled", hkw.texture.Image("data/lroc_color_poles_8k.png"))
)
hkw.render(base, config, filename="results/moon.png")

# Render back side.
config.emitters[0].rotation = 90
config.sensor.location = [-3, 0, 0]
hkw.render(base, config, filename="results/moon_backside.png")
