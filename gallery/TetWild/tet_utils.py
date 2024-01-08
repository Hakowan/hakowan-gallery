# Utility functions for tetrahedral meshes.
# Note taht the `mtet` package used in this script has not been released yet.
# It will become public hopefully after Siggraph 2024 deadline.

from os import PathLike
import mtet
import lagrange
import numpy as np


def load_tet_mesh(filename: PathLike) -> mtet.MTetMesh:
    """Load a tetrahedral mesh from a file.

    Args:
        filename: Path to the file to load.

    Returns:
        A tuple containing the vertices and tetrahedra of the mesh.
    """
    return mtet.load_mesh(str(filename))


def extract_boundary(tet_mesh: mtet.MTetMesh):
    """Extract the boundary of a tetrahedral mesh.

    Args:
        tet_mesh: The tetrahedral mesh to extract the boundary from.

    Returns:
        A lagrange SurfaceMesh object representing the boundary triangle mesh.
    """
    vertices = []
    triangles = []
    vertex_map = {}

    def process_vertices(vertex_id: mtet.VertexId):
        coords = tet_mesh.get_vertex(vertex_id)
        vertices.append(coords)
        vertex_map[vertex_id.value] = len(vertices) - 1

    def process_tets(tet_id: mtet.TetId):
        tet_vts = tet_mesh.get_tet(tet_id)
        assert tet_mesh.has_vertex(tet_vts[0])
        assert tet_mesh.has_vertex(tet_vts[1])
        assert tet_mesh.has_vertex(tet_vts[2])
        assert tet_mesh.has_vertex(tet_vts[3])
        v0 = vertex_map[tet_vts[0].value]
        v1 = vertex_map[tet_vts[1].value]
        v2 = vertex_map[tet_vts[2].value]
        v3 = vertex_map[tet_vts[3].value]

        m0 = tet_mesh.get_mirror(tet_id, 0)
        m1 = tet_mesh.get_mirror(tet_id, 1)
        m2 = tet_mesh.get_mirror(tet_id, 2)
        m3 = tet_mesh.get_mirror(tet_id, 3)

        if not tet_mesh.has_tet(m0):
            triangles.append([v1, v2, v3])
        if not tet_mesh.has_tet(m1):
            triangles.append([v0, v3, v2])
        if not tet_mesh.has_tet(m2):
            triangles.append([v0, v1, v3])
        if not tet_mesh.has_tet(m3):
            triangles.append([v0, v2, v1])

    tet_mesh.seq_foreach_vertex(process_vertices)
    tet_mesh.seq_foreach_tet(process_tets)

    vertices = np.array(vertices)
    triangles = np.array(triangles)

    mesh = lagrange.SurfaceMesh()
    mesh.add_vertices(vertices)
    mesh.add_triangles(triangles)

    return mesh


def extract_clipped_boundary(tet_mesh: mtet.MTetMesh, clip_fn):
    """Extract the boundary of a clipped tetrahedral mesh.

    Args:
        tet_mesh: The tetrahedral mesh to extract the boundary from.
        clip_fn: A clip function that takes a 3D point and returns True if the
            point is inside the non-clipped region.

    Returns:
        A lagrange SurfaceMesh object representing the boundary of the clipped mesh.
        The mesh contains the `boundary_tag` facet attribute, which is 1 if and only if the triangle
        is on the clipped boundary.
    """
    vertices = []
    triangles = []
    vertex_map = {}
    triangle_tags = []

    def process_vertices(vertex_id: mtet.VertexId):
        coords = tet_mesh.get_vertex(vertex_id)
        vertices.append(coords)
        vertex_map[vertex_id.value] = len(vertices) - 1

    def compute_tet_centroid(tet_id: mtet.TetId):
        tet_vts = tet_mesh.get_tet(tet_id)
        v0 = vertex_map[tet_vts[0].value]
        v1 = vertex_map[tet_vts[1].value]
        v2 = vertex_map[tet_vts[2].value]
        v3 = vertex_map[tet_vts[3].value]
        c = np.mean([vertices[v0], vertices[v1], vertices[v2], vertices[v3]], axis=0)
        return c

    def _should_keep(tet_id: mtet.TetId):
        c = compute_tet_centroid(tet_id)
        return clip_fn(c)

    def process_tets(tet_id: mtet.TetId):
        assert tet_mesh.has_tet(tet_id)
        tet_vts = tet_mesh.get_tet(tet_id)
        assert tet_mesh.has_vertex(tet_vts[0])
        assert tet_mesh.has_vertex(tet_vts[1])
        assert tet_mesh.has_vertex(tet_vts[2])
        assert tet_mesh.has_vertex(tet_vts[3])
        v0 = vertex_map[tet_vts[0].value]
        v1 = vertex_map[tet_vts[1].value]
        v2 = vertex_map[tet_vts[2].value]
        v3 = vertex_map[tet_vts[3].value]
        c = np.mean([vertices[v0], vertices[v1], vertices[v2], vertices[v3]], axis=0)
        if not clip_fn(c):
            return

        m0 = tet_mesh.get_mirror(tet_id, 0)
        m1 = tet_mesh.get_mirror(tet_id, 1)
        m2 = tet_mesh.get_mirror(tet_id, 2)
        m3 = tet_mesh.get_mirror(tet_id, 3)

        if not tet_mesh.has_tet(m0):
            triangles.append([v1, v2, v3])
            triangle_tags.append(0)
        elif not _should_keep(m0):
            triangles.append([v1, v2, v3])
            triangle_tags.append(1)

        if not tet_mesh.has_tet(m1):
            triangles.append([v0, v3, v2])
            triangle_tags.append(0)
        elif not _should_keep(m1):
            triangles.append([v0, v3, v2])
            triangle_tags.append(1)

        if not tet_mesh.has_tet(m2):
            triangles.append([v0, v1, v3])
            triangle_tags.append(0)
        elif not _should_keep(m2):
            triangles.append([v0, v1, v3])
            triangle_tags.append(1)

        if not tet_mesh.has_tet(m3):
            triangles.append([v0, v2, v1])
            triangle_tags.append(0)
        elif not _should_keep(m3):
            triangles.append([v0, v2, v1])
            triangle_tags.append(1)

    tet_mesh.seq_foreach_vertex(process_vertices)
    tet_mesh.seq_foreach_tet(process_tets)

    vertices = np.array(vertices)
    triangles = np.array(triangles)
    triangle_tags = np.array(triangle_tags)

    mesh = lagrange.SurfaceMesh()
    mesh.add_vertices(vertices)
    mesh.add_triangles(triangles)
    mesh.create_attribute(
        "boundary_tag",
        element=lagrange.AttributeElement.Facet,
        usage=lagrange.AttributeUsage.Scalar,
        initial_values=triangle_tags,
    )

    return mesh
