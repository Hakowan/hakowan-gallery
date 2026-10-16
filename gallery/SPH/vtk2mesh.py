#!/usr/bin/env python

import pyvista as pv
import numpy as np
import lagrange

for idx in [133, 10, 60, 30]:
    mesh = pv.read(f"data/ParticleData_Fluid_0_{idx}.vtk")
    vertices = np.array(mesh.points)
    velocities = np.array(mesh.point_data["velocity"])

    lmesh = lagrange.SurfaceMesh()
    lmesh.add_vertices(vertices)
    lmesh.create_attribute(
        "velocity",
        element=lagrange.AttributeElement.Vertex,
        usage=lagrange.AttributeUsage.Vector,
        initial_values=velocities,
    )

    lagrange.io.save_mesh(f"data/waterbell_{idx:03d}.pcd", lmesh)
