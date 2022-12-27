"""
This module contains functions for generating four-body geometries found in
the HCP lattice, where 3 of the 6 side lengths of each geometry are equal to
the lattice constant. There are 17 of these geometries.

Recall that a four-body geometry has 6 relative pair distances between all
of its points. The 17 geometries in this module are related in that, of these
6 pair distances, 3 of them are equal to the lattice constant. The other 3
are larger.

Unlike the case for the geometries where 4 or 5 of the side lengths are equal
to the lattice constant, each sorted 6-tuple of side lengths can sometimes have
two different geometries associated with it. I have arbitrarily attached a
letter 'a' or 'b' to distinguish them.
"""

from cartesian import Cartesian3D
from cartesian import CartesianND

from hydro4b_coords.geometries.checker import _check_lat_const_positive


def fourbody_geometry_sqrt2_sqrt2_sqrt83(lat_const: float) -> list[CartesianND]:
    """
    Points for the four-body geometry with the relative pair distances
    (1, 1, 1, sqrt(2), sqrt(2), sqrt(8/3)).
    """
    _check_lat_const_positive(lat_const)

    return [
        lat_const * Cartesian3D(0.000000, 0.000000, 0.000000),
        lat_const * Cartesian3D(0.500000, 0.866025, 0.000000),
        lat_const * Cartesian3D(0.000000, 1.154701, 0.816497),
        lat_const * Cartesian3D(0.000000, 1.154701, -0.816497),
    ]


def fourbody_geometry_sqrt2_sqrt2_sqrt113(lat_const: float) -> list[CartesianND]:
    """
    Points for the four-body geometry with the relative pair distances
    (1, 1, 1, sqrt(2), sqrt(2), sqrt(11/3)).
    """
    _check_lat_const_positive(lat_const)

    return [
        lat_const * Cartesian3D(0.000000, 0.000000, 0.000000),
        lat_const * Cartesian3D(0.500000, 0.866025, 0.000000),
        lat_const * Cartesian3D(0.000000, 1.154701, 0.816497),
        lat_const * Cartesian3D(-0.500000, 0.288675, -0.816497),
    ]


def fourbody_geometry_sqrt2_sqrt2_2(lat_const: float) -> list[CartesianND]:
    """
    Points for the four-body geometry with the relative pair distances
    (1, 1, 1, sqrt(2), sqrt(2), 2).
    """
    _check_lat_const_positive(lat_const)

    return [
        lat_const * Cartesian3D(0.000000, 0.000000, 0.000000),
        lat_const * Cartesian3D(0.500000, 0.866025, 0.000000),
        lat_const * Cartesian3D(0.000000, 1.154701, 0.816497),
        lat_const * Cartesian3D(1.000000, 1.732051, 0.000000),
    ]


def fourbody_geometry_sqrt2_sqrt83_sqrt113(lat_const: float) -> list[CartesianND]:
    """
    Points for the four-body geometry with the relative pair distances
    (1, 1, 1, sqrt(2), sqrt(8/3), sqrt(11/3)).
    """
    _check_lat_const_positive(lat_const)

    return [
        lat_const * Cartesian3D(0.000000, 0.000000, 0.000000),
        lat_const * Cartesian3D(0.500000, 0.866025, 0.000000),
        lat_const * Cartesian3D(0.000000, 1.154701, 0.816497),
        lat_const * Cartesian3D(0.500000, 0.866025, 1.632993),
    ]


def fourbody_geometry_sqrt2_sqrt3_sqrt3_a(lat_const: float) -> list[CartesianND]:
    """
    Points for the 'a'-version four-body geometry with the relative pair distances
    (1, 1, 1, sqrt(2), sqrt(3), sqrt(3)).
    """
    _check_lat_const_positive(lat_const)

    return [
        lat_const * Cartesian3D(0.000000, 0.000000, 0.000000),
        lat_const * Cartesian3D(0.500000, 0.866025, 0.000000),
        lat_const * Cartesian3D(0.000000, 1.154701, 0.816497),
        lat_const * Cartesian3D(0.000000, -0.577350, 0.816497),
    ]


def fourbody_geometry_sqrt2_sqrt3_sqrt3_b(lat_const: float) -> list[CartesianND]:
    """
    Points for the 'b'-version four-body geometry with the relative pair distances
    (1, 1, 1, sqrt(2), sqrt(3), sqrt(3)).
    """
    _check_lat_const_positive(lat_const)

    return [
        lat_const * Cartesian3D(0.000000, 0.000000, 0.000000),
        lat_const * Cartesian3D(0.500000, 0.866025, 0.000000),
        lat_const * Cartesian3D(0.000000, 1.154701, 0.816497),
        lat_const * Cartesian3D(1.500000, 0.866025, 0.000000),
    ]


def fourbody_geometry_sqrt2_sqrt3_sqrt113_a(lat_const: float) -> list[CartesianND]:
    """
    Points for the 'a'-version four-body geometry with the relative pair distances
    (1, 1, 1, sqrt(2), sqrt(3), sqrt(11/3)).
    """
    _check_lat_const_positive(lat_const)

    return [
        lat_const * Cartesian3D(0.000000, 0.000000, 0.000000),
        lat_const * Cartesian3D(0.500000, 0.866025, 0.000000),
        lat_const * Cartesian3D(0.500000, 0.288675, 0.816497),
        lat_const * Cartesian3D(1.500000, 0.288675, -0.816497),
    ]


def fourbody_geometry_sqrt2_sqrt3_sqrt113_b(lat_const: float) -> list[CartesianND]:
    """
    Points for the 'b'-version four-body geometry with the relative pair distances
    (1, 1, 1, sqrt(2), sqrt(3), sqrt(11/3)).
    """
    _check_lat_const_positive(lat_const)

    return [
        lat_const * Cartesian3D(0.000000, 0.000000, 0.000000),
        lat_const * Cartesian3D(0.500000, 0.866025, 0.000000),
        lat_const * Cartesian3D(0.000000, 1.154701, 0.816497),
        lat_const * Cartesian3D(1.000000, 1.154701, -0.816497),
    ]


def fourbody_geometry_sqrt2_sqrt113_sqrt113_a(lat_const: float) -> list[CartesianND]:
    """
    Points for the 'a'-version four-body geometry with the relative pair distances
    (1, 1, 1, sqrt(2), sqrt(11/3), sqrt(11/3)).
    """
    _check_lat_const_positive(lat_const)

    return [
        lat_const * Cartesian3D(0.000000, 0.000000, 0.000000),
        lat_const * Cartesian3D(0.500000, 0.866025, 0.000000),
        lat_const * Cartesian3D(0.500000, 0.288675, 0.816497),
        lat_const * Cartesian3D(-0.500000, 0.866025, 1.632993),
    ]


def fourbody_geometry_sqrt2_sqrt113_sqrt113_b(lat_const: float) -> list[CartesianND]:
    """
    Points for the 'b'-version four-body geometry with the relative pair distances
    (1, 1, 1, sqrt(2), sqrt(11/3), sqrt(11/3)).
    """
    _check_lat_const_positive(lat_const)

    return [
        lat_const * Cartesian3D(0.000000, 0.000000, 0.000000),
        lat_const * Cartesian3D(0.500000, 0.866025, 0.000000),
        lat_const * Cartesian3D(0.000000, 1.154701, 0.816497),
        lat_const * Cartesian3D(-0.500000, 0.866025, 1.632993),
    ]


def fourbody_geometry_sqrt83_sqrt3_sqrt3(lat_const: float) -> list[CartesianND]:
    """
    Points for the four-body geometry with the relative pair distances
    (1, 1, 1, sqrt(8/3), sqrt(3), sqrt(3)).
    """
    _check_lat_const_positive(lat_const)

    return [
        lat_const * Cartesian3D(0.000000, 0.000000, 0.000000),
        lat_const * Cartesian3D(0.500000, 0.866025, 0.000000),
        lat_const * Cartesian3D(0.000000, -0.577350, 0.816497),
        lat_const * Cartesian3D(0.000000, -0.577350, -0.816497),
    ]


def fourbody_geometry_sqrt83_sqrt3_sqrt113(lat_const: float) -> list[CartesianND]:
    """
    Points for the four-body geometry with the relative pair distances
    (1, 1, 1, sqrt(8/3), sqrt(3), sqrt(11/3)).
    """
    _check_lat_const_positive(lat_const)

    return [
        lat_const * Cartesian3D(0.000000, 0.000000, 0.000000),
        lat_const * Cartesian3D(0.500000, 0.866025, 0.000000),
        lat_const * Cartesian3D(0.000000, 0.000000, 1.632993),
        lat_const * Cartesian3D(0.000000, -0.577350, 0.816497),
    ]


def fourbody_geometry_sqrt83_sqrt113_sqrt113(lat_const: float) -> list[CartesianND]:
    """
    Points for the four-body geometry with the relative pair distances
    (1, 1, 1, sqrt(8/3), sqrt(11/3), sqrt(11/3)).
    """
    _check_lat_const_positive(lat_const)

    return [
        lat_const * Cartesian3D(0.000000, 0.000000, 0.000000),
        lat_const * Cartesian3D(0.500000, 0.866025, 0.000000),
        lat_const * Cartesian3D(0.000000, 0.000000, 1.632993),
        lat_const * Cartesian3D(1.000000, 0.000000, 0.000000),
    ]


def fourbody_geometry_sqrt3_sqrt3_sqrt3_a(lat_const: float) -> list[CartesianND]:
    """
    Points for the 'a'-version four-body geometry with the relative pair distances
    (1, 1, 1, sqrt(3), sqrt(3), sqrt(3)).
    """
    _check_lat_const_positive(lat_const)

    return [
        lat_const * Cartesian3D(0.000000, 0.000000, 0.000000),
        lat_const * Cartesian3D(0.500000, 0.866025, 0.000000),
        lat_const * Cartesian3D(0.500000, 0.288675, 0.816497),
        lat_const * Cartesian3D(-1.000000, 1.154701, 0.816497),
    ]


def fourbody_geometry_sqrt3_sqrt3_sqrt3_b(lat_const: float) -> list[CartesianND]:
    """
    Points for the 'b'-version four-body geometry with the relative pair distances
    (1, 1, 1, sqrt(3), sqrt(3), sqrt(3)).
    """
    _check_lat_const_positive(lat_const)

    return [
        lat_const * Cartesian3D(0.000000, 0.000000, 0.000000),
        lat_const * Cartesian3D(0.500000, 0.866025, 0.000000),
        lat_const * Cartesian3D(0.000000, 1.732051, 0.000000),
        lat_const * Cartesian3D(1.500000, 0.866025, 0.000000),
    ]


def fourbody_geometry_sqrt3_sqrt3_2_a(lat_const: float) -> list[CartesianND]:
    """
    Points for the 'a'-version four-body geometry with the relative pair distances
    (1, 1, 1, sqrt(3), sqrt(3), 2).
    """
    _check_lat_const_positive(lat_const)

    return [
        lat_const * Cartesian3D(0.000000, 0.000000, 0.000000),
        lat_const * Cartesian3D(0.500000, 0.866025, 0.000000),
        lat_const * Cartesian3D(0.500000, 0.288675, 0.816497),
        lat_const * Cartesian3D(1.500000, -0.866025, 0.000000),
    ]


def fourbody_geometry_sqrt3_sqrt3_2_b(lat_const: float) -> list[CartesianND]:
    """
    Points for the 'b'-version four-body geometry with the relative pair distances
    (1, 1, 1, sqrt(3), sqrt(3), 2).
    """
    _check_lat_const_positive(lat_const)

    return [
        lat_const * Cartesian3D(0.000000, 0.000000, 0.000000),
        lat_const * Cartesian3D(0.500000, 0.866025, 0.000000),
        lat_const * Cartesian3D(0.000000, 1.732051, 0.000000),
        lat_const * Cartesian3D(-1.000000, 0.000000, 0.000000),
    ]
