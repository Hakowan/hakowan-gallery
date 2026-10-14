#!/usr/bin/env python

import math

import hakowan as hkw

hkw.set_default_backend("mitsuba")

FRAME_NUMBERS = (7, 8, 9, 10)
CAMERA_SCALE = 1.5625
PLATE_PATH = "data/plate2.obj"
INTERACTIVE_BALL_PATH = "data/10_decimated.msh"

# Step 1:
# Create a ball layer. The ball geometry is specified later.
# Approximate the original IPC figure with pinkish material.
# Note that Hakowan supports any valid CSS color name or hex code.
#
# See [CSS colors](https://www.w3schools.com/cssref/css_colors.php).

ball = hkw.layer().material("RoughPlastic", "salmon", alpha=0.02)

# Step 2:
# Create a plate layer containing the collision plate.
# Use glass-like material so one can see the collision-induced deformation clearly.

plate = hkw.layer(PLATE_PATH).material("ThinDielectric")

# Step 3: Render!
# We have 4 different results sampled at different time during the simulation.
# We will create two visualizations for each result: side view and back view.


def make_figure(layer):
    return hkw.Figure(layer).camera("orthographic", scale=CAMERA_SCALE)


for frame_number in FRAME_NUMBERS:
    frame_scene = ball.data(f"data/{frame_number}.obj") + plate
    side_figure = make_figure(frame_scene)

    # The side view shows the ball-plate collision from the side.
    hkw.render(
        side_figure,
        filename=f"results/ipc_side_{frame_number}.webp",
    )

    # The back view shows the ball-plate collision from behind the plate.
    back_scene = frame_scene.rotate(axis=[0, 1, 0], angle=-math.pi / 2)
    hkw.render(
        make_figure(back_scene),
        filename=f"results/ipc_back_{frame_number}.webp",
    )

RECIPE_FIGURE = side_figure
RECIPE_INSPECTIONS = {"ball": INTERACTIVE_BALL_PATH, "plate": PLATE_PATH}

interactive_scene = ball.data(INTERACTIVE_BALL_PATH) + plate
hkw.render(
    make_figure(interactive_scene),
    backend="webgl",
    filename="results/ipc.html",
)
