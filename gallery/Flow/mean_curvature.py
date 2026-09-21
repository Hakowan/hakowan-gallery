#!/usr/bin/env python

import igl
from scipy.sparse.linalg import spsolve
import scipy as sp
import numpy as np
import lagrange

v, f = igl.read_triangle_mesh("data/bust.ply")
cotangent_laplacian = igl.cotmatrix(v, f)
mass_matrix = igl.massmatrix(v, f, igl.MASSMATRIX_TYPE_VORONOI)
minv = sp.sparse.diags(1 / mass_matrix.diagonal())

v0 = v

for i in range(10):
    mass_matrix = igl.massmatrix(v, f, igl.MASSMATRIX_TYPE_BARYCENTRIC)
    system = mass_matrix - 0.1 * cotangent_laplacian
    v = spsolve(system, mass_matrix.dot(v))

    mesh = lagrange.SurfaceMesh()
    mesh.add_vertices(v)
    mesh.add_triangles(f)

    k = igl.gaussian_curvature(v, f)
    kn = minv.dot(k)
    dist = np.linalg.norm(v - v0, axis=1)
    print(np.min(kn), np.max(kn))
    mesh.create_attribute(
        "dist",
        element=lagrange.AttributeElement.Vertex,
        usage=lagrange.AttributeUsage.Scalar,
        initial_values=dist,
    )
    mesh.create_attribute(
        "curvature",
        element=lagrange.AttributeElement.Vertex,
        usage=lagrange.AttributeUsage.Scalar,
        initial_values=kn,
    )

    lagrange.io.save_mesh(f"data/flow_{i:02}.ply", mesh)
