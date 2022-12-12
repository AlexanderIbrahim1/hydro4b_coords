"""
This module contains functions for generating 8 of the four-body geometries
found in the HCP lattice.

Recall that a four-body geometry has 6 relative pair distances between all
of its points. The 8 geometries in this module are related in that, of these
6 pair distances, 4 of them are equal to the lattice constant. The other two
are larger. Unlike the four-body geometries where 5 of the 6 pair separations
are equal, there does not seem to be an easy way to relate all of them.

These functions are named based on the ratio of each of the two longer pair
distances to the lattice constant. For example, the geometry where the side
lengths are (for a lattice constant 1)

        (1, 1, 1, 1, sqrt(2), sqrt(3))

is named 'fourbody_geometry_sqrt2_sqrt3()'.
"""

import math

from cartesian import Cartesian3D
from cartesian import CartesianND

from hydro4b_coords.geometries.checker import _check_lat_const_positive


def fourbody_geometry_sqrt2_sqrt2(lat_const: float) -> list[CartesianND]:
    """
    Points for the four-body geometry with the relative pair distances
    (1, 1, 1, 1, sqrt(2), sqrt(2)).
    """
    _check_lat_const_positive(lat_const)

    return [
        lat_const * Cartesian3D(0.0, 0.0, 0.0),
        lat_const * Cartesian3D(1.0, 0.0, 0.0),
        lat_const * Cartesian3D(0.0, 1.0, 0.0),
        lat_const * Cartesian3D(1.0, 1.0, 0.0),
    ]


def fourbody_geometry_sqrt2_sqrt3(lat_const: float) -> list[CartesianND]:
    """
    Points for the four-body geometry with the relative pair distances
    (1, 1, 1, 1, sqrt(2), sqrt(3)).
    """
    _check_lat_const_positive(lat_const)

    return [
        lat_const * Cartesian3D(0.0, 0.0, 0.0),
        lat_const * Cartesian3D(0.5, math.sqrt(3.0 / 4.0), 0.0),
        lat_const * Cartesian3D(0.0, math.sqrt(3.0 / 1.0), 0.0),
        lat_const * Cartesian3D(0.0, math.sqrt(4.0 / 3.0), math.sqrt(2.0 / 3.0)),
    ]


def fourbody_geometry_sqrt3_sqrt3(lat_const: float) -> list[CartesianND]:
    """
    Points for the four-body geometry with the relative pair distances
    (1, 1, 1, 1, sqrt(3), sqrt(3)).
    """
    _check_lat_const_positive(lat_const)

    return [
        lat_const * Cartesian3D(0.0, 0.0, 0.0),
        lat_const * Cartesian3D(0.5, math.sqrt(3.0 / 4.0), 0.0),
        lat_const * Cartesian3D(-0.5, math.sqrt(3.0 / 4.0), 0.0),
        lat_const * Cartesian3D(0.0, -math.sqrt(1.0 / 3.0), math.sqrt(2.0 / 3.0)),
    ]


def fourbody_geometry_sqrt3_2(lat_const: float) -> list[CartesianND]:
    """
    Points for the four-body geometry with the relative pair distances
    (1, 1, 1, 1, sqrt(3), 2).
    """
    _check_lat_const_positive(lat_const)

    return [
        lat_const * Cartesian3D(-1.0, 0.0, 0.0),
        lat_const * Cartesian3D(0.0, 0.0, 0.0),
        lat_const * Cartesian3D(1.0, 0.0, 0.0),
        lat_const * Cartesian3D(0.5, math.sqrt(3.0 / 4.0), 0.0),
    ]


def fourbody_geometry_sqrt2_sqrt113(lat_const: float) -> list[CartesianND]:
    """
    Points for the four-body geometry with the relative pair distances
    (1, 1, 1, 1, sqrt(2), sqrt(11/3)).
    """
    _check_lat_const_positive(lat_const)

    return [
        lat_const * Cartesian3D(0.0, 0.0, math.sqrt(8.0 / 3.0)),
        lat_const * Cartesian3D(0.0, math.sqrt(1.0 / 3.0), math.sqrt(2.0 / 3.0)),
        lat_const * Cartesian3D(0.5, math.sqrt(3.0 / 4.0), 0.0),
        lat_const * Cartesian3D(1.0, math.sqrt(1.0 / 3.0), math.sqrt(2.0 / 3.0)),
    ]


def fourbody_geometry_sqrt3_sqrt113(lat_const: float) -> list[CartesianND]:
    """
    Points for the four-body geometry with the relative pair distances
    (1, 1, 1, 1, sqrt(3), sqrt(11/3)).
    """
    _check_lat_const_positive(lat_const)

    return [
        lat_const * Cartesian3D(0.0, 0.0, math.sqrt(8.0 / 3.0)),
        lat_const * Cartesian3D(0.0, math.sqrt(1.0 / 3.0), math.sqrt(2.0 / 3.0)),
        lat_const * Cartesian3D(0.5, math.sqrt(3.0 / 4.0), 0.0),
        lat_const * Cartesian3D(0.5, math.sqrt(25.0 / 12.0), math.sqrt(2.0 / 3.0)),
    ]


def fourbody_geometry_sqrt83_sqrt113(lat_const: float) -> list[CartesianND]:
    """
    Points for the four-body geometry with the relative pair distances
    (1, 1, 1, 1, sqrt(8/3), sqrt(11/3)).
    """
    _check_lat_const_positive(lat_const)

    return [
        lat_const * Cartesian3D(0.0, 0.0, math.sqrt(8.0 / 3.0)),
        lat_const * Cartesian3D(0.0, math.sqrt(1.0 / 3.0), math.sqrt(2.0 / 3.0)),
        lat_const * Cartesian3D(0.5, math.sqrt(3.0 / 4.0), 0.0),
        lat_const * Cartesian3D(0.0, 0.0, 0.0),
    ]


def fourbody_geometry_sqrt113_sqrt113(lat_const: float) -> list[CartesianND]:
    """
    Points for the four-body geometry with the relative pair distances
    (1, 1, 1, 1, sqrt(11/3), sqrt(11/3)).
    """
    _check_lat_const_positive(lat_const)

    return [
        lat_const * Cartesian3D(0.0, 0.0, math.sqrt(8.0 / 3.0)),
        lat_const * Cartesian3D(0.0, math.sqrt(1.0 / 3.0), math.sqrt(2.0 / 3.0)),
        lat_const * Cartesian3D(0.5, math.sqrt(3.0 / 4.0), 0.0),
        lat_const * Cartesian3D(-0.5, math.sqrt(3.0 / 4.0), 0.0),
    ]
