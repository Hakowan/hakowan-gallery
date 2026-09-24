#!/usr/bin/env python

import hakowan as hkw
import pyvista as pv
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
    # Lagrange's MSH writer does not retain vertex attributes on facet-free
    # point clouds. Load the original VTK particles so velocity reaches the
    # Norm transform and ScalarField colormap.
    particles = pv.read(f"data/ParticleData_Fluid_0_{i}.vtk")
    particle_frame = hkw.dataframe.to_dataframe(particles, roi_box=roi_box)
    fluid = (
        hkw.layer()
        .name(f"Fluid {i:03}")
        .data(particle_frame)
        .mark("Point")
        .channel(size=0.01)
        .material(
            "Principled",
            hkw.texture.ScalarField(
                "speed", domain=[0, 10], legend=hkw.Legend(title="Speed")
            ),
        )
    ).transform(hkw.transform.Norm("velocity", "speed"))
    all_particles = hkw.Figure(fluid + emitter, scene)
    if i == 10:
        RECIPE_FIGURE = all_particles
        RECIPE_INSPECTIONS = {
            "particles": particles,
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
