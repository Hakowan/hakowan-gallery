#!/usr/bin/env python

import hakowan as hkw
import lagrange

# Step 1:
# Create a ball layer containing the ball geometry.
# Approximate the original IPC figure with pinkish material.
ball = hkw.layer("data/7.obj").channel(
    material=hkw.material.RoughPlastic("salmon", alpha=0.02)
)

# Step 2:
# Create a plate layer containing the collision plate.
# Use glass-like material so one can see the collision-induced deformation clearly.

# The plate geometry has very skinny triangles. Mitsuba has trouble computing accurate normal for
# this mesh. Thus, we explicitly generates the correct normal and use it in the normal channel.
plate_mesh = lagrange.io.load_mesh("data/plate.obj")
normal_id = lagrange.compute_normal(plate_mesh)
normal_name = plate_mesh.get_attribute_name(normal_id)

plate = hkw.layer(plate_mesh).channel(
    normal=normal_name, material=hkw.material.ThinDielectric()
)

# Step 3: Adjust configuration.
config = hkw.config()
# Use orthographic camera for better visualization of the collision.
config.sensor = hkw.setup.sensor.Orthographic()
# Use volume path integrator to reduce rendering noise.
config.integrator = hkw.setup.integrator.VolPath()

# Step 4: Render!
# The side view shows the ball-plate collision from the side.
hkw.render(ball + plate, config, filename="results/ipc_side.png")

# The back view shows the ball-plate collision from behind the plate.
config.sensor.location = [5, 0, 0]
hkw.render(ball + plate, config, filename="results/ipc_back.png")
