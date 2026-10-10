#!/usr/bin/env python

import lagrange
import numpy as np

torus = lagrange.primitive.generate_torus(
    triangulate=True, major_radius=1.0, minor_radius=0.4
)
bvh = lagrange.bvh.TriangleAABBTree3D(torus)
query = bvh.get_closest_point([2, 0, 0])

samples, _, _ = lagrange.sampling.sample_blue_noise(torus, num_samples=1000)

engine = lagrange.geodesic.GeodesicEngineFlip(torus)

paths = []
for i, p in enumerate(samples):
    fid, bc, _ = bvh.get_closest_point(p.tolist())
    geo_path = engine.point_to_point_geodesic_path(query[0], fid, query[1][1:], bc[1:])
    pts, facets = geo_path
    pts = np.array(pts, dtype=np.float64)
    path = lagrange.SurfaceMesh()
    path.add_vertices(pts)
    edges = np.array([[i, i + 1] for i in range(len(pts) - 1)], dtype=np.uint32)
    path.add_polygons(edges)
    path.create_attribute("id", initial_values=np.full(len(pts), i))

    paths.append(path)

geodesic_path = lagrange.combine_meshes(paths)
geodesic_path.create_attribute(
    "line_id", initial_values=np.ones(geodesic_path.num_facets, dtype=np.uint32)
)


lagrange.io.save_mesh("data/donut.obj", torus)
lagrange.io.save_mesh("data/geodesics.obj", geodesic_path)
