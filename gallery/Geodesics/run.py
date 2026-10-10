#!/usr/bin/env python

import lagrange
import hakowan as hkw
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

base = hkw.layer(torus).material("ThinDielectric").name("Torus")
paths = (
    hkw.layer(geodesic_path)
    .mark("Curve")
    .channel(size=hkw.channel.Size(3, space="screen"))
    .name("Geodesic Paths")
)
paths = paths.material(
    "Principled", hkw.texture.ScalarField("id", categories=True, legend=False)
)

fig = (
    hkw.Figure(base + paths)
    .camera("perspective", up=[0, 0, 1], eye=[0, -3, 0])
    .environment(up=(0, 0, 1))
)
#hkw.render(fig, filename="geodesic_path.html")
#hkw.render(fig, backend="mitsuba", filename="geodesic_path.webp")
