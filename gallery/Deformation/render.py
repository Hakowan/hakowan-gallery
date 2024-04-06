#!/usr/bin/env python

import hakowan as hkw

# Handle layer with rough plastic material.
handles = (
    hkw.layer()
    .material("RoughPlastic", "steelblue")
    .transform(hkw.transform.Filter(data="label", condition=lambda x: x in [1, 2]))
)

# Deformed region with smooth conductor material.
deformed_region = (
    hkw.layer()
    .material("Conductor", "Hg")
    .transform(hkw.transform.Filter(data="label", condition=lambda x: x == 0))
)

# Create four different layers with different inptu data.
l1 = (handles + deformed_region).data("data/cylinder_1.msh")
l2 = (handles + deformed_region).data("data/cylinder_2.msh")
l3 = (handles + deformed_region).data("data/cylinder_3.msh")
l4 = (handles + deformed_region).data("data/cylinder_4.msh")

# Render the layers.
config = hkw.config()
config.z_up()
config.sensor.location = (0, -3, 0)
hkw.render(l1, config, filename="results/cylinder_1.png")
hkw.render(l2, config, filename="results/cylinder_2.png")
hkw.render(l3, config, filename="results/cylinder_3.png")
hkw.render(l4, config, filename="results/cylinder_4.png")
