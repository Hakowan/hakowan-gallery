#!/usr/bin/env python

import lagrange
import numpy as np
import math

# Constants
sqrt_2 = math.sqrt(2)
sqrt_3 = math.sqrt(3)

# Tet vertices
v0 = np.array([0, 0, 0])
v1 = np.array([1, 0, 0])
v2 = np.array([0.5, sqrt_3 / 2, 0])
v3 = np.array([0.5, sqrt_3 / 6, sqrt_2 / sqrt_3])

# Edge vertices
e01 = (v0 + v1) / 2
e02 = (v0 + v2) / 2
e03 = (v0 + v3) / 2
e12 = (v1 + v2) / 2
e13 = (v1 + v3) / 2
e23 = (v2 + v3) / 2

# Face vertices
f012 = (v0 + v1 + v2) / 3
f013 = (v0 + v1 + v3) / 3
f023 = (v0 + v2 + v3) / 3
f123 = (v1 + v2 + v3) / 3

# Tet center
c = (v0 + v1 + v2 + v3) / 4


def generate_tet(v, e, f, c, flip=False):
    tet = lagrange.SurfaceMesh()
    tet.add_vertex(v)
    tet.add_vertex(e)
    tet.add_vertex(f)
    tet.add_vertex(c)
    if not flip:
        tet.add_triangle(0, 1, 2)
        tet.add_triangle(3, 2, 1)
        tet.add_triangle(3, 1, 0)
        tet.add_triangle(3, 0, 2)
    else:
        tet.add_triangle(0, 2, 1)
        tet.add_triangle(3, 1, 2)
        tet.add_triangle(3, 0, 1)
        tet.add_triangle(3, 2, 0)

    tet.create_attribute(
        "vertex_label",
        element=lagrange.AttributeElement.Vertex,
        usage=lagrange.AttributeUsage.Scalar,
        initial_values=np.array([0, 1, 2, 3]),
    )
    return tet


# Generate sub tets.
tets = [
    generate_tet(v0, e01, f012, c, True),
    generate_tet(v1, e01, f012, c, False),
    generate_tet(v1, e12, f012, c, True),
    generate_tet(v2, e12, f012, c, False),
    generate_tet(v2, e02, f012, c, True),
    generate_tet(v0, e02, f012, c, False),
    generate_tet(v1, e12, f123, c, False),
    generate_tet(v2, e12, f123, c, True),
    generate_tet(v2, e23, f123, c, False),
    generate_tet(v3, e23, f123, c, True),
    generate_tet(v3, e13, f123, c, False),
    generate_tet(v1, e13, f123, c, True),
    generate_tet(v0, e01, f013, c, False),
    generate_tet(v1, e01, f013, c, True),
    generate_tet(v1, e13, f013, c, False),
    generate_tet(v3, e13, f013, c, True),
    generate_tet(v3, e03, f013, c, False),
    generate_tet(v0, e03, f013, c, True),
    generate_tet(v2, e02, f023, c, False),
    generate_tet(v0, e02, f023, c, True),
    generate_tet(v0, e03, f023, c, False),
    generate_tet(v3, e03, f023, c, True),
    generate_tet(v3, e23, f023, c, False),
    generate_tet(v2, e23, f023, c, True),
]

combined = lagrange.combine_meshes(tets)
lagrange.io.save_mesh("data/powell_sabin.ply", combined)
