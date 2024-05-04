#!/usr/bin/env python

import hakowan as hkw
import math

# Step 1:
# Create a ball layer. The ball geometry will be speicified later.
# Approximate the original IPC figure with pinkish material.
# Note that Hakowan supports any valid CSS color names as well as hex code codes.
#
# See [CSS colors](https://www.w3schools.com/cssref/css_colors.php).

ball = hkw.layer().material("RoughPlastic", "salmon", alpha=0.02)

# Step 2:
# Create a plate layer containing the collision plate.
# Use glass-like material so one can see the collision-induced deformation clearly.

plate = hkw.layer("data/plate2.obj").material("ThinDielectric")

# Step 3: Adjust configuration.
# For this visualization, it is best to use orthographic projection and avoid perspective
# distortion.

config = hkw.config()
# Use orthographic camera for better visualization of the collision.
config.sensor = hkw.setup.sensor.Orthographic()
# Use volume path integrator to reduce rendering noise.
config.integrator = hkw.setup.integrator.VolPath()

# Step 4: Render!
# We have 4 different results sampled at different time during the simulation.
# We will create two visualizations for each result: side view and back view.

for i in [7, 8, 9, 10]:
    # Set the data component of the ball layer.
    ball = ball.data(f"data/{i}.obj")

    # The side view shows the ball-plate collision from the side.
    side_view = ball + plate
    hkw.render(side_view, config, filename=f"results/ipc_side_{i}.png")

    # The back view shows the ball-plate collision from behind the plate.
    # Rotation matrix to rotate around y-axis by 90 degrees.
    back_view = (ball + plate).rotate(axis=[0, 1, 0], angle=-math.pi / 2)
    hkw.render(back_view, config, filename=f"results/ipc_back_{i}.png")
