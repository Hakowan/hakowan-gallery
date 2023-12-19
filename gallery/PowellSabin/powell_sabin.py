#!/usr/bin/env python

import lagrange
import hakowan as hkw

mesh = lagrange.io.load_mesh("data/powell_sabin.ply")
normal_id = lagrange.compute_facet_normal(mesh)
normal_name = mesh.get_attribute_name(normal_id)

num_comps = lagrange.compute_components(mesh, "comp_ids")

base = hkw.layer(mesh).channel(normal=normal_name)

vertices = base.mark(hkw.mark.Point).channel(
    material=hkw.material.Principled(
        color=hkw.texture.ScalarField(
            "vertex_label", colormap=["steelblue", "green", "yellow", "red"]
        ),
        roughness=0,
        metallic=0.3,
    ),
    size=0.015,
)
edges = base.mark(hkw.mark.Curve).channel(
    material=hkw.material.Conductor("Cr"), size=0.005
)
surface = base.mark(hkw.mark.Surface).channel(
    material=hkw.material.Principled(
        color=hkw.texture.ScalarField("comp_ids", colormap="set1", categories=num_comps)
    )
)

config = hkw.config()
config.z_up()
config.sensor.location = [2.5, -2.5, 0]
hkw.render(vertices + edges + surface, config, filename="results/powell_sabin.png")

exploded_view = (vertices + edges + surface).transform(
    hkw.transform.Explode("comp_ids", magnitude=0.5)
)
config.sensor.location = [2.5, -2.5, 0]
hkw.render(exploded_view, config, filename="results/powell_sabin_explode.png")
