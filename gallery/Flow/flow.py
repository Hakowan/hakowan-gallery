#!/usr/bin/env python
import copy

import hakowan as hkw

hkw.set_default_backend("webgl")

flow0 = hkw.layer("data/flow_00.ply").name("Surface 0")
flow9 = hkw.layer("data/flow_09.ply").name("Surface 9")

s = 0.3
mat = hkw.material.Principled(
    hkw.texture.ScalarField(
        hkw.attribute(
            "dist",
            scale=hkw.scale.Normalize(
                domain_min=0, domain_max=s, range_min=0, range_max=1
            ),
        ),
        legend=False,
    ),
    roughness=0.2,
    metallic=0.2,
)

legend_mat = copy.deepcopy(mat)
legend_mat.color.legend = hkw.Legend(title="Distance")

dist0 = flow0.name("Distance 0").channel(material=legend_mat)
dist9 = flow9.name("Distance 9").channel(material=copy.deepcopy(mat))

comp = flow0.compare(flow9, gap=-0.4, labels=["itr 0", "itr 9"])
mix0 = hkw.grid([flow0, dist0], columns=2, column_gap=-0.4)
mix9 = hkw.grid([flow9, dist9], columns=2, column_gap=-0.4)
comp_all = hkw.grid([flow0, dist0, flow9, dist9], columns=4)

scene = hkw.SceneSettings(
    camera=hkw.PerspectiveCamera(eye=(0, -4, 0), up=(0, 0, 1)),
    environment=hkw.Environment(up=(0, 0, 1)),
    output=hkw.OutputSettings(width=1000, height=800),
)
RECIPE_FIGURE = hkw.Figure(comp_all, scene)
RECIPE_INSPECTIONS = {
    "initial-surface": "data/flow_00.ply",
    "final-surface": "data/flow_09.ply",
}

hkw.render(
    hkw.Figure(comp, scene), backend="mitsuba", filename="results/bust_comp.webp"
)
hkw.render(hkw.Figure(mix0, scene), backend="mitsuba", filename="results/bust_00.webp")
hkw.render(hkw.Figure(mix9, scene), backend="mitsuba", filename="results/bust_09.webp")

hkw.render(RECIPE_FIGURE, filename="results/bust_all.html")
