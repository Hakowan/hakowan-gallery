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

# Polyharmonic operators of increasing order: L, -L·M⁻¹·L, L·M⁻¹·L·M⁻¹·L, ...
laplacians = [L]
for _ in range(3):
    laplacians.append(-laplacians[-1] * MI * L)

num_constraints = len(handle_indices)
C = scipy.sparse.coo_matrix(
    (np.ones(num_constraints), (np.arange(num_constraints), handle_indices)),
    shape=(num_constraints, mesh.num_vertices),
)

b = np.zeros((mesh.num_vertices + num_constraints, 3))
b[-num_constraints:] = handle_pos

for i, Lk in enumerate(laplacians, start=1):
    kkt = scipy.sparse.bmat([[Lk, C.transpose()], [C, None]]).tocsc()
    vertices = scipy.sparse.linalg.spsolve(kkt, b)[: mesh.num_vertices]
    mesh.vertices[:] = vertices
    lagrange.io.save_mesh(f"data/cylinder_{i}.msh", mesh)
