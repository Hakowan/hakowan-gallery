#!/usr/bin/env python

import pyvista as pv
import numpy as np
import lagrange

#mesh = pv.read("ParticleData_Fluid_0_133.vtk")
#mesh = pv.read("ParticleData_Fluid_0_10.vtk")
#mesh = pv.read("ParticleData_Fluid_0_60.vtk")
mesh = pv.read("ParticleData_Fluid_0_30.vtk")

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

lagrange.io.save_mesh("waterbell_030.msh", lmesh)
