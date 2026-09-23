#!/usr/bin/env python

import lagrange

mesh = lagrange.io.load_mesh("data/shark.msh")
mesh = mesh.clone(strip=True)

ops = lagrange.polyddg.DifferentialOperators(mesh)
lagrange.polyddg.compute_smooth_direction_field(
    mesh, ops, output_element_type=lagrange.AttributeElement.Facet
)

lagrange.io.save_mesh("shark.msh", mesh)
