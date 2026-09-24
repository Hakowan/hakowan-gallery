#!/usr/bin/env python
import copy

import hakowan as hkw

hkw.set_default_backend("webgl")

flow0 = hkw.layer("data/flow_00.ply").name("Surface 0")
flow2 = hkw.layer("data/flow_02.ply").name("Surface 2")
flow5 = hkw.layer("data/flow_05.ply").name("Surface 5")
flow9 = hkw.layer("data/flow_09.ply").name("Surface 9")

s = 0.3
mat = hkw.material.Principled(
    hkw.texture.ScalarField(
        hkw.attribute(
            "dist",
            scale=hkw.scale.Normalize(
                domain_min=-s, domain_max=s, range_min=0, range_max=1
            ),
        ),
        legend=False,
    ),
    roughness=0.5,
    metallic=0.2,
)

legend_mat = copy.deepcopy(mat)
legend_mat.color.legend = hkw.Legend(title="Distance")

dist0 = flow0.name("Distance 0").channel(material=legend_mat)
dist2 = flow2.name("Distance 2").channel(material=copy.deepcopy(mat))
dist5 = flow5.name("Distance 5").channel(material=copy.deepcopy(mat))
dist9 = flow9.name("Distance 9").channel(material=copy.deepcopy(mat))

comparison = (dist0 | dist2 | dist5 | dist9).compare(
    flow0 | flow2 | flow5 | flow9,
    axis="z",
)
scene = hkw.SceneSettings(
    camera=hkw.PerspectiveCamera(eye=(0, -2.5, 0), up=(0, 0, 1)),
    environment=hkw.Environment(up=(0, 0, 1)),
    output=hkw.OutputSettings(width=600, height=1024),
)
RECIPE_FIGURE = hkw.Figure(comparison, scene)
RECIPE_INSPECTIONS = {"surface": "data/flow_00.ply"}

hkw.render(RECIPE_FIGURE, backend="mitsuba", filename="results/bust.webp")
hkw.render(RECIPE_FIGURE, filename="results/bust_all.html")
