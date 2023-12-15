#!/usr/bin/env python3

import hakowan as hkw
import pathlib
import scipy
import numpy as np

# Generate base layer setting.
# We are using image-based texture for color in this example.
# The UV is scaled by 10 times for visualizaiton purposes.
base = hkw.layer().channel(
    material=hkw.material.Principled(
        color=hkw.texture.Image(
            filename=pathlib.Path("data/texture.png"),
            uv=hkw.attribute("texcoord", scale=10),
        ),
        roughness=0.2,
    )
)

# Figure 3
fig3 = base.data("data/fig3.obj")

# Minor adjustment of the camera and light.
config = hkw.config()
config.sensor.location = (0, 0, -4)
config.emitters[0].rotation = 0

hkw.render(fig3, config, filename="results/fig3.png")

# Figure 10

# The input mesh comes at an odd orientation.
# We apply affine transform to fix the orientation issue.
M = np.eye(4, dtype=np.float64)
M[:3, :3] = scipy.spatial.transform.Rotation.from_euler(
    "x", -45, degrees=True
).as_matrix()
fig10 = base.data("data/fig10_uniform.obj").transform(hkw.transform.Affine(M))

# Again, fine tuning the camera and light.
config.y_up()
config.sensor.location = (-3, 0, -3)
config.emitters[0].rotation = 0

hkw.render(fig10, config, filename="results/fig10.png")
