import lagrange
import numpy as np


def load_data():
    # The ref mesh contains the base geometry.
    ref_mesh = lagrange.io.load_mesh("data/teaser_pig_bnb_target.obj")

    # Chain mesh contains the layout boundaries.
    # Each chain is a sequence of ref mesh vertices.
    chains_mesh = lagrange.SurfaceMesh()
    chains_mesh.add_vertices(ref_mesh.vertices)

    # Load chains from the .lem file.
    chains = []
    with open("data/teaser_pig_bnb.lem", "r") as fin:
        for line in fin:
            if line.startswith("ee"):
                chain = line.split(":")[1].split()
                chain = [int(i) for i in chain]
                chains.append(chain)

    # Add chains to the chain mesh.
    for chain in chains:
        for i in range(len(chain) - 1):
            chains_mesh.add_polygon(np.array([chain[i], chain[i + 1]]))

    # Compute layout charts.
    involved_vertices = np.unique(np.hstack(chains)).tolist()
    lagrange.compute_components(
        ref_mesh,
        output_attribute_name="chart",
        connectivity_type=lagrange.ConnectivityType.Vertex,
        blocker_elements=involved_vertices,
    )

    return ref_mesh, chains_mesh
