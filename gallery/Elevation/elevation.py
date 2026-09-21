#!/usr/bin/env python

import hakowan as hkw
from image2mesh import image2mesh

hkw.set_default_backend("mitsuba")

# Step 1: Generate a mesh from a heightmap.
usgs_data = image2mesh("data/USGS_1_n35w112.tif")


# Step 2: Create a map layer that maps elevation to color.
# Note that we use a custom colormap here.
def elevation_layer(data):
    return (
        hkw.layer(data)
        .material(
            "Principled",
            hkw.texture.ScalarField(
                "elevation",
                colormap=["#15A887", "#8C4E37", "#E9ECF2"],
                legend=hkw.Legend(title="Elevation"),
            ),
        )
        .transform(hkw.transform.Compute(z="elevation"))
    )


usgs_map = elevation_layer(usgs_data)

# Step 3: Render from two different angles.
front = hkw.figure(usgs_map).camera("perspective", eye=(0, 0, 3))
RECIPE_FIGURE = front
RECIPE_INSPECTIONS = {"terrain": usgs_data}
RECIPE_DATA_IDS = {id(usgs_data): "terrain"}
hkw.render(front, filename="results/usgs_1_n35112.webp")

side = hkw.figure(usgs_map).camera("perspective", eye=(0, -2, 2))
hkw.render(side, filename="results/usgs_1_n35112_side.webp")

# Step 4: Export a downsampled front view as an interactive WebGL demo.
interactive_data = image2mesh(
    "data/USGS_1_n35w112.tif",
    max_dimension=256,
)
interactive = hkw.figure(elevation_layer(interactive_data)).camera(
    "perspective", eye=(0, 0, 3)
)
hkw.render(interactive, backend="webgl", filename="results/usgs_1_n35112.html")
