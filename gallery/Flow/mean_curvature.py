#!/usr/bin/env python

import igl
from scipy.sparse.linalg import spsolve
import scipy as sp
import numpy as np
from matplotlib.pyplot import subplot
import lagrange

v, f = igl.read_triangle_mesh("data/bust.ply")
l = igl.cotmatrix(v, f)
m = igl.massmatrix(v, f, igl.MASSMATRIX_TYPE_VORONOI)
minv = sp.sparse.diags(1 / m.diagonal())

n = igl.per_vertex_normals(v, f) * 0.5 + 0.5
c = np.linalg.norm(n, axis=1)

v0 = v

vs = [v]
cs = [c]
for i in range(10):
    m = igl.massmatrix(v, f, igl.MASSMATRIX_TYPE_BARYCENTRIC)
    s = m - 0.1 * l
    b = m.dot(v)
    v = spsolve(s, m.dot(v))
    n = igl.per_vertex_normals(v, f) * 0.5 + 0.5
    c = np.linalg.norm(n, axis=1)
    vs.append(v)
    cs.append(c)

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
