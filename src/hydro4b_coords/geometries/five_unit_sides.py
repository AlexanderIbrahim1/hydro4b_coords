"""
This module contains functions for generating 3 of the four-body geometries
found in the HCP lattice.

Recall that a four-body geometry has 6 relative pair distances between all
of its points. The 3 geometries in this module are related in that, of these
6 pair distances, 5 of them are equal to the lattice constant. The last side
is larger.

These functions are named based on the ratio of each of the two longer pair
distances to the lattice constant. For example, the geometry where the side
lengths are (for a lattice constant 1)

        (1, 1, 1, 1, 1, sqrt(2))

is named 'fourbody_geometry_sqrt2()'.
"""

import math

from cartesian import Cartesian3D
from cartesian import CartesianND

from hydro4b_coords.geometries.checker import _check_lat_const_positive


def fourbody_geometry_sqrt2(lat_const: float) -> list[CartesianND]:
    irregular_tetrahedron_angle = 2.0 * math.asin(math.sqrt(2.0 / 3.0))
    return irregular_tetrahedron(lat_const, irregular_tetrahedron_angle)


def fourbody_geometry_sqrt83(lat_const: float) -> list[CartesianND]:
    irregular_tetrahedron_angle = 2.0 * math.asin(math.sqrt(8.0 / 9.0))
    return irregular_tetrahedron(lat_const, irregular_tetrahedron_angle)


def fourbody_geometry_sqrt3(lat_const: float) -> list[CartesianND]:
    irregular_tetrahedron_angle = 2.0 * math.asin(1.0)
    return irregular_tetrahedron(lat_const, irregular_tetrahedron_angle)


def irregular_tetrahedron(
    lat_const: float, irregular_tetrahedron_angle: float
) -> list[CartesianND]:
    """
    The 3 four-body geometries in the HCP lattice, where five of the side lengths
    are equal to the lattice constant, can be related to each other by a single
    internal angle (in radians) in the geometry.
    """
    _check_lat_const_positive(lat_const)

    equil_tri_height = math.sqrt(3.0 / 4.0)
    y_pos = equil_tri_height * math.cos(irregular_tetrahedron_angle)
    z_pos = equil_tri_height * math.sin(irregular_tetrahedron_angle)

    return [
        lat_const * Cartesian3D(-0.5, 0.0, 0.0),
        lat_const * Cartesian3D(0.5, 0.0, 0.0),
        lat_const * Cartesian3D(0.0, math.sqrt(3.0 / 4.0), 0.0),
        lat_const * Cartesian3D(0.0, y_pos, z_pos),
    ]


# aliases to keep the previous function calls working
irregular_tetrahedron_sqrt2 = fourbody_geometry_sqrt2
irregular_tetrahedron_sqrt83 = fourbody_geometry_sqrt83
irregular_tetrahedron_sqrt3 = fourbody_geometry_sqrt3
