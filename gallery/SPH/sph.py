#!/usr/bin/env python

import hakowan as hkw
import numpy as np
from hakowan.spec import compile_expression

hkw.set_default_backend("mitsuba")

scene = hkw.SceneSettings(camera=hkw.PerspectiveCamera(eye=(0, 0, 3)))


def _recipe_data_id(_mesh):
    return "particles"


emitter = (
    hkw.layer("data/emitter.msh")
    .name("Emitter")
    .channel(material=hkw.material.RoughPlastic("Ivory"))
)

box_min = [-1.223, -0.5, -1.226]
box_max = [1.224, 4.0, 1.222]
roi_box = np.vstack([box_min, box_max])
for i in [10, 30, 60, 133]:
    particle_file = f"data/waterbell_{i:03}.pcd"
    fluid = (
        hkw.layer().data(particle_file, roi_box=roi_box)
        .name(f"Fluid {i:03}")
        .mark("Point")
        .channel(size=0.01)
        .material(
            "Principled",
            hkw.texture.ScalarField(
                "speed", domain=[0, 10], legend=False,
            ),
        )
    ).transform(hkw.transform.Norm("velocity", "speed"))
    all_particles = hkw.Figure(fluid + emitter, scene)
    if i == 10:
        RECIPE_FIGURE = all_particles
        RECIPE_INSPECTIONS = {
            "particles": particle_file,
            "emitter": "data/emitter.msh",
        }
        RECIPE_DATA_IDS = _recipe_data_id
    hkw.render(all_particles, filename=f"results/waterbell_{i:03}_all.webp")
    hkw.render(
        all_particles,
        backend="webgl",
        filename=f"results/waterbell_{i:03}_all.html",
    )

    filtered = fluid.transform(
        hkw.transform.Filter(condition=compile_expression("z <= 0"))
    )
    filtered_particles = hkw.Figure(filtered + emitter, scene)
    hkw.render(filtered_particles, filename=f"results/waterbell_{i:03}.webp")
    hkw.render(
        filtered_particles,
        backend="webgl",
        filename=f"results/waterbell_{i:03}.html",
    )
