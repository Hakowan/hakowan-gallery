#!/usr/bin/env python

import hakowan as hkw

# Step 1:
# Create a ball layer containing the ball geometry.
# Approximate the original IPC figure with pinkish material.

ball = hkw.layer("data/7.obj").channel(
    material=hkw.material.RoughPlastic("salmon", alpha=0.02)
)

# Step 2:
# Create a plate layer containing the collision plate.
# Use glass-like material so one can see the collision-induced deformation clearly.

plate = hkw.layer("data/plate.obj").channel(material=hkw.material.ThinDielectric())

# Step 3: Adjust configuration.

config = hkw.config()
# Use orthographic camera for better visualization of the collision.
config.sensor = hkw.setup.sensor.Orthographic()
# Use volume path integrator to reduce rendering noise.
config.integrator = hkw.setup.integrator.VolPath()

# Step 4: Render!

# The side view shows the ball-plate collision from the side.
side_view = ball + plate
hkw.render(side_view, config, filename="results/ipc_side.png")

# The back view shows the ball-plate collision from behind the plate.

# Rotation matrix to rotate around y-axis by 90 degrees.
rotate_y90 = [
    [0, 0, -1],
    [0, 1, 0],
    [1, 0, 0],
]
back_view = (ball + plate).transform(hkw.transform.Affine(rotate_y90))
hkw.render(back_view, config, filename="results/ipc_back.png")
