#!/usr/bin/env python

import igl
import lagrange
import numpy as np
import scipy.sparse

mesh = lagrange.io.load_mesh("data/cylinder.ply")
lagrange.remove_duplicate_vertices(mesh)
orig_vertices = mesh.vertices.copy()

handle_top = np.nonzero(mesh.vertices[:, 2] >= 2)
handle_bot = np.nonzero(mesh.vertices[:, 2] <= -2)

handle_top_pos = mesh.vertices[handle_top]
handle_bot_pos = mesh.vertices[handle_bot]

vertex_labels = np.zeros(mesh.num_vertices, dtype=np.int32)
vertex_labels[handle_top] = 1
vertex_labels[handle_bot] = 2
facet_labels = vertex_labels[mesh.facets].min(axis=1)
mesh.create_attribute(
    "label",
    element=lagrange.AttributeElement.Facet,
    usage=lagrange.AttributeUsage.Scalar,
    initial_values=facet_labels,
)

handle_top_pos[:, 0] *= -1
handle_top_pos[:, [0, 2]] = handle_top_pos[:, [2, 0]]
handle_top_pos[:, 0] += 1.0
handle_top_pos[:, 2] += 1.0

handle_indices = np.concatenate((handle_top, handle_bot), axis=1).ravel()
handle_pos = np.concatenate(
    (
        handle_top_pos,
        handle_bot_pos,
    ),
    axis=0,
)

L = igl.cotmatrix(mesh.vertices, mesh.facets.astype(np.int64))
M = igl.massmatrix(
    mesh.vertices, mesh.facets.astype(np.int64), igl.MASSMATRIX_TYPE_VORONOI
)
MI = scipy.sparse.diags(1.0 / M.diagonal())

L2 = -L * MI * L
L3 = -L2 * MI * L
L4 = L3 * MI * L


num_constraints = len(handle_indices)
C = scipy.sparse.coo_matrix(
    (np.ones(num_constraints), (np.arange(num_constraints), handle_indices)),
    shape=(num_constraints, mesh.num_vertices),
)

M = scipy.sparse.bmat([[L, C.transpose()], [C, None]]).tocsc()
M2 = scipy.sparse.bmat([[L2, C.transpose()], [C, None]]).tocsc()
M3 = scipy.sparse.bmat([[L3, C.transpose()], [C, None]]).tocsc()
M4 = scipy.sparse.bmat([[L4, C.transpose()], [C, None]]).tocsc()

b = np.zeros((mesh.num_vertices + num_constraints, 3))
b[-num_constraints:] = handle_pos

vertices = scipy.sparse.linalg.spsolve(M, b)[: mesh.num_vertices]
mesh.vertices[:] = vertices
lagrange.io.save_mesh("data/cylinder_1.msh", mesh)

vertices = scipy.sparse.linalg.spsolve(M2, b)[: mesh.num_vertices]
mesh.vertices[:] = vertices
lagrange.io.save_mesh("data/cylinder_2.msh", mesh)

vertices = scipy.sparse.linalg.spsolve(M3, b)[: mesh.num_vertices]
mesh.vertices[:] = vertices
lagrange.io.save_mesh("data/cylinder_3.msh", mesh)

vertices = scipy.sparse.linalg.spsolve(M4, b)[: mesh.num_vertices]
mesh.vertices[:] = vertices
lagrange.io.save_mesh("data/cylinder_4.msh", mesh)
