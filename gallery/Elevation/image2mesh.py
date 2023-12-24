#!/usr/bin/env python

from PIL import Image
import numpy as np
import lagrange
import pathlib

def image2mesh(filename: pathlib.Path):
    """Generate a height field mesh from a grayscale image.

    Args:
        filename: The path to the image file.

    Returns:
        A lagrange SurfaceMesh object representing the height field.
    """
    im = Image.open(filename)
    w,h = im.size

    x, y = np.meshgrid(np.arange(w), np.arange(h))
    x = x.ravel()
    y = y.ravel()
    z = np.array(im).ravel() / 5
    vertices = np.ascontiguousarray(np.vstack([x, y, z]).T)

    facets = []
    for i in range(h-1):
        for j in range(w-1):
            v0 = i * w + j
            v1 = i * w + j + 1
            v2 = (i + 1) * w + j
            v3 = (i + 1) * w + j + 1
            facets.append([v0, v1, v3, v2])
    facets = np.array(facets)

    mesh = lagrange.SurfaceMesh()
    mesh.add_vertices(vertices)
    mesh.add_quads(facets)
    return mesh
