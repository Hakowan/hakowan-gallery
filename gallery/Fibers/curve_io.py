from os import PathLike
import numpy as np
import lagrange


def load_curves(filename: PathLike):
    vertices = []
    edges = []
    curve_id = []
    curve_count = 0
    with open(filename, "r") as fin:
        for line in fin:
            if line.startswith("v "):
                vertices.append([float(val) for val in line.strip().split()[1:]])
            elif line.startswith("l "):
                chain = [int(val) - 1 for val in line.strip().split()[1:]]
                for i in range(len(chain) - 1):
                    edges.append((chain[i], chain[i + 1]))
                    curve_id.append(curve_count)
                curve_count += 1

    vertices = np.array(vertices)
    edges = np.array(edges)

    mesh = lagrange.SurfaceMesh()
    mesh.add_vertices(vertices)
    mesh.add_polygons(edges)
    mesh.create_attribute(
        "curve_id",
        element=lagrange.AttributeElement.Facet,
        usage=lagrange.AttributeUsage.Scalar,
        initial_values=np.asarray(curve_id),
    )

    return mesh
