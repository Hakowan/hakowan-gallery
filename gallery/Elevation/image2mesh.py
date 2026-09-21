#!/usr/bin/env python

from PIL import Image
import numpy as np
import lagrange
import pathlib


def image2mesh(filename: pathlib.Path, *, max_dimension: int | None = None):
    """Generate a height field mesh from a grayscale image.

    Args:
        filename: The path to the image file.
        max_dimension: Optionally downsample the image while preserving its world extent.

    Returns:
        A lagrange SurfaceMesh object representing the height field.
    """
    im = Image.open(filename)
    original_w, original_h = im.size
    if max_dimension is not None and max(original_w, original_h) > max_dimension:
        scale = max_dimension / max(original_w, original_h)
        im = im.resize(
            (
                max(2, round(original_w * scale)),
                max(2, round(original_h * scale)),
            ),
            Image.Resampling.BILINEAR,
        )
    w, h = im.size

    x_coordinates = np.linspace(0, original_w - 1, w)
    y_coordinates = np.linspace(0, original_h - 1, h)
    x, y = np.meshgrid(x_coordinates, y_coordinates)
    x = x.ravel()
    y = y.ravel()
    z = np.array(im).ravel() / 5
    vertices = np.ascontiguousarray(np.vstack([x, y, z]).T)

    facets = []
    for i in range(h - 1):
        for j in range(w - 1):
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
