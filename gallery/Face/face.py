#!/usr/bin/env python

import hakowan as hkw

# Step 1: Setup the configurtion for portrait.
config = hkw.config()
config.film.width = 800
config.film.height = 1024
config.sensor.location = [1.0, 0.5, 3]

# Step 2: Render the 3D face mesh.
face = hkw.layer("data/canonical_face_model.obj")
hkw.render(face, config, filename="results/face.png")

# Step 3: Render the 3D face mesh with checkerboard pattern.
face_checkerboard = face.channel(
    material=hkw.material.Principled(
        color=hkw.texture.Checkerboard(size=8),
        roughness=0.1,
    )
)
hkw.render(face_checkerboard, config, filename="results/face_checkerboard.png")

# Step 4: Render the UV mesh with 3D normal field.
face_uv = (
    face.transform(hkw.transform.UVMesh())
    .transform(hkw.transform.Compute(vertex_normal="normal"))
    .channel(normal="normal", material=hkw.material.Diffuse("ivory"))
)
config.film.width = 1024
config.film.height = 800
config.sensor = hkw.setup.sensor.Orthographic()
hkw.render(face_uv, config, filename="results/face_uv.png")
