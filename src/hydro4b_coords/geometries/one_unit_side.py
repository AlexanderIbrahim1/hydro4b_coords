"""
This module contains functions for generating four-body geometries found in
the HCP lattice, where 1 of the 6 side lengths of each geometry is equal to
the lattice constant. There are 35 of these geometries.

Recall that a four-body geometry has 6 relative pair distances between all
of its points. The 19 geometries in this module are related in that, of these
6 pair distances, 1 of them are equal to the lattice constant. The other 4
are larger.

Unlike the case for the geometries where 4 or 5 of the side lengths are equal
to the lattice constant, each sorted 6-tuple of side lengths can sometimes have
multiple different geometries associated with it. I have arbitrarily attached a
letter 'a', 'b', 'c, ... to distinguish them.
"""

from cartesian import Cartesian3D
from cartesian import CartesianND

from hydro4b_coords.geometries.checker import _check_lat_const_positive


def fourbody_geometry_sqrt2_sqrt2_sqrt83_sqrt3_sqrt3(
    lat_const: float,
) -> list[CartesianND]:
    """
    Points for the four-body geometry with the relative pair distances
    (1, sqrt(2), sqrt(2), sqrt(8/3), sqrt(3), sqrt(3))
    # (1.000000, 1.414214, 1.414214, 1.632993, 1.732051, 1.732051)
    """
    _check_lat_const_positive(lat_const)
    points = [
        (0.000000, 0.000000, 0.000000),
        (0.500000, 0.866025, 0.000000),
        (1.500000, 0.288675, 0.816497),
        (1.500000, 0.288675, -0.816497),
    ]

    return [lat_const * Cartesian3D(*p) for p in points]


def fourbody_geometry_sqrt2_sqrt2_sqrt83_sqrt3_sqrt113(
    lat_const: float,
) -> list[CartesianND]:
    """
    Points for the four-body geometry with the relative pair distances
    (1, sqrt(2), sqrt(2), sqrt(8/3), sqrt(3), sqrt(11/3))
    # (1.000000, 1.414214, 1.414214, 1.632993, 1.732051, 1.914854)
    """
    _check_lat_const_positive(lat_const)
    points = [
        (0.000000, 0.000000, 0.000000),
        (0.500000, 0.866025, 0.000000),
        (0.000000, 0.000000, 1.632993),
        (1.000000, -0.577350, 0.816497),
    ]

    return [lat_const * Cartesian3D(*p) for p in points]


def fourbody_geometry_sqrt2_sqrt2_sqrt3_sqrt3_sqrt113_a(
    lat_const: float,
) -> list[CartesianND]:
    """
    Points for the 'a'-version of the four-body geometry with the relative pair distances
    (1, sqrt(2), sqrt(2), sqrt(3), sqrt(3), sqrt(11/3))
    # (1.000000, 1.414214, 1.414214, 1.732051, 1.732051, 1.914854)
    """
    _check_lat_const_positive(lat_const)
    points = [
        (0.000000, 0.000000, 0.000000),
        (0.500000, 0.866025, 0.000000),
        (1.500000, 0.288675, 0.816497),
        (1.000000, -0.577350, -0.816497),
    ]

    return [lat_const * Cartesian3D(*p) for p in points]


def fourbody_geometry_sqrt2_sqrt2_sqrt3_sqrt3_sqrt113_b(
    lat_const: float,
) -> list[CartesianND]:
    """
    Points for the 'b'-version of the four-body geometry with the relative pair distances
    (1, sqrt(2), sqrt(2), sqrt(3), sqrt(3), sqrt(11/3))
    # (1.000000, 1.414214, 1.414214, 1.732051, 1.732051, 1.914854)
    """
    _check_lat_const_positive(lat_const)
    points = [
        (0.000000, 0.000000, 0.000000),
        (0.500000, 0.288675, 0.816497),
        (0.000000, 1.154701, -0.816497),
        (1.500000, 0.866025, 0.000000),
    ]

    return [lat_const * Cartesian3D(*p) for p in points]


def fourbody_geometry_sqrt2_sqrt2_sqrt3_sqrt3_2(lat_const: float) -> list[CartesianND]:
    """
    Points for the four-body geometry with the relative pair distances
    (1, sqrt(2), sqrt(2), sqrt(3), sqrt(3), 2)
    # (1.000000, 1.414214, 1.414214, 1.732051, 1.732051, 2.000000)
    """
    _check_lat_const_positive(lat_const)
    points = [
        (0.000000, 0.000000, 0.000000),
        (0.500000, 0.866025, 0.000000),
        (1.500000, 0.288675, 0.816497),
        (1.500000, -0.866025, 0.000000),
    ]

    return [lat_const * Cartesian3D(*p) for p in points]


def fourbody_geometry_sqrt2_sqrt2_sqrt3_sqrt113_2(
    lat_const: float,
) -> list[CartesianND]:
    """
    Points for the four-body geometry with the relative pair distances
    (1, sqrt(2), sqrt(2), sqrt(3), sqrt(11/3), 2)
    # (1.000000, 1.414214, 1.414214, 1.732051, 1.914854, 2.000000)
    """
    _check_lat_const_positive(lat_const)
    points = [
        (0.000000, 0.000000, 0.000000),
        (0.500000, 0.288675, 0.816497),
        (0.000000, 1.154701, -0.816497),
        (1.000000, 1.732051, 0.000000),
    ]

    return [lat_const * Cartesian3D(*p) for p in points]


def fourbody_geometry_sqrt2_sqrt2_sqrt113_sqrt113_2(
    lat_const: float,
) -> list[CartesianND]:
    """
    Points for the four-body geometry with the relative pair distances
    (1, sqrt(2), sqrt(2), sqrt(11/3), sqrt(11/3), 2)
    # (1.000000, 1.414214, 1.414214, 1.914854, 1.914854, 2.000000)
    """
    _check_lat_const_positive(lat_const)
    points = [
        (0.000000, 0.000000, 0.000000),
        (0.500000, 0.288675, 0.816497),
        (0.000000, 1.154701, -0.816497),
        (1.000000, -0.577350, -0.816497),
    ]

    return [lat_const * Cartesian3D(*p) for p in points]


def fourbody_geometry_sqrt2_sqrt83_sqrt3_sqrt3_sqrt113(
    lat_const: float,
) -> list[CartesianND]:
    """
    Points for the four-body geometry with the relative pair distances
    (1, sqrt(2), sqrt(8/3), sqrt(3), sqrt(3), sqrt(11/3))
    # (1.000000, 1.414214, 1.632993, 1.732051, 1.732051, 1.914854)
    """
    _check_lat_const_positive(lat_const)
    points = [
        (0.000000, 0.000000, 0.000000),
        (0.500000, 0.866025, 0.000000),
        (0.000000, 0.000000, 1.632993),
        (1.500000, 0.288675, 0.816497),
    ]

    return [lat_const * Cartesian3D(*p) for p in points]


def fourbody_geometry_sqrt2_sqrt3_sqrt3_sqrt3_sqrt3_a(
    lat_const: float,
) -> list[CartesianND]:
    """
    Points for the 'a'-version of the four-body geometry with the relative pair distances
    (1, sqrt(2), sqrt(3), sqrt(3), sqrt(3), sqrt(3))
    # (1.000000, 1.414214, 1.732051, 1.732051, 1.732051, 1.732051)
    """
    _check_lat_const_positive(lat_const)
    points = [
        (0.000000, 0.000000, 0.000000),
        (0.500000, 0.288675, 0.816497),
        (0.000000, 1.732051, 0.000000),
        (1.500000, 0.866025, 0.000000),
    ]

    return [lat_const * Cartesian3D(*p) for p in points]


def fourbody_geometry_sqrt2_sqrt3_sqrt3_sqrt3_sqrt3_b(
    lat_const: float,
) -> list[CartesianND]:
    """
    Points for the 'b'-version of the four-body geometry with the relative pair distances
    (1, sqrt(2), sqrt(3), sqrt(3), sqrt(3), sqrt(3))
    # (1.000000, 1.414214, 1.732051, 1.732051, 1.732051, 1.732051)
    """
    _check_lat_const_positive(lat_const)
    points = [
        (0.000000, 0.000000, 0.000000),
        (0.500000, 0.288675, 0.816497),
        (0.000000, 1.732051, 0.000000),
        (-1.000000, 1.154701, 0.816497),
    ]

    return [lat_const * Cartesian3D(*p) for p in points]


def fourbody_geometry_sqrt2_sqrt3_sqrt3_sqrt3_sqrt113(
    lat_const: float,
) -> list[CartesianND]:
    """
    Points for the four-body geometry with the relative pair distances
    (1, sqrt(2), sqrt(3), sqrt(3), sqrt(3), sqrt(11/3))
    # (1.000000, 1.414214, 1.732051, 1.732051, 1.732051, 1.914854)
    """
    _check_lat_const_positive(lat_const)
    points = [
        (0.000000, 0.000000, 0.000000),
        (0.500000, 0.288675, 0.816497),
        (0.000000, 1.732051, 0.000000),
        (1.000000, 1.154701, -0.816497),
    ]

    return [lat_const * Cartesian3D(*p) for p in points]


def fourbody_geometry_sqrt2_sqrt3_sqrt3_sqrt113_sqrt113_a(
    lat_const: float,
) -> list[CartesianND]:
    """
    Points for the 'a'-version of the four-body geometry with the relative pair distances
    (1, sqrt(2), sqrt(3), sqrt(3), sqrt(11/3), sqrt(11/3))
    # (1.000000, 1.414214, 1.732051, 1.732051, 1.914854, 1.914854)
    """
    _check_lat_const_positive(lat_const)
    points = [
        (0.000000, 0.000000, 0.000000),
        (0.500000, 0.288675, 0.816497),
        (0.000000, 1.154701, -0.816497),
        (1.500000, 0.288675, -0.816497),
    ]

    return [lat_const * Cartesian3D(*p) for p in points]


def fourbody_geometry_sqrt2_sqrt3_sqrt3_sqrt113_sqrt113_b(
    lat_const: float,
) -> list[CartesianND]:
    """
    Points for the 'b'-version of the four-body geometry with the relative pair distances
    (1, sqrt(2), sqrt(3), sqrt(3), sqrt(11/3), sqrt(11/3))
    # (1.000000, 1.414214, 1.732051, 1.732051, 1.914854, 1.914854)
    """
    _check_lat_const_positive(lat_const)
    points = [
        (0.000000, 0.000000, 0.000000),
        (0.500000, 0.288675, 0.816497),
        (0.000000, 1.154701, -0.816497),
        (-1.000000, 1.154701, 0.816497),
    ]

    return [lat_const * Cartesian3D(*p) for p in points]


def fourbody_geometry_sqrt83_sqrt3_sqrt3_sqrt3_sqrt3(
    lat_const: float,
) -> list[CartesianND]:
    """
    Points for the four-body geometry with the relative pair distances
    (1, sqrt(8/3), sqrt(3), sqrt(3), sqrt(3), sqrt(3))
    # (1.000000, 1.632993, 1.732051, 1.732051, 1.732051, 1.732051)
    """
    _check_lat_const_positive(lat_const)
    points = [
        (0.000000, 0.000000, 0.000000),
        (0.500000, 0.866025, 0.000000),
        (-1.000000, 1.154701, 0.816497),
        (-1.000000, 1.154701, -0.816497),
    ]

    return [lat_const * Cartesian3D(*p) for p in points]


def fourbody_geometry_sqrt83_sqrt3_sqrt3_sqrt3_sqrt113(
    lat_const: float,
) -> list[CartesianND]:
    """
    Points for the four-body geometry with the relative pair distances
    (1, sqrt(8/3), sqrt(3), sqrt(3), sqrt(3), sqrt(11/3))
    # (1.000000, 1.632993, 1.732051, 1.732051, 1.732051, 1.914854)
    """
    _check_lat_const_positive(lat_const)
    points = [
        (0.000000, 0.000000, 0.000000),
        (0.500000, 0.866025, 0.000000),
        (0.000000, 0.000000, 1.632993),
        (-1.000000, 1.154701, 0.816497),
    ]

    return [lat_const * Cartesian3D(*p) for p in points]


def fourbody_geometry_sqrt3_sqrt3_sqrt3_sqrt113_2(
    lat_const: float,
) -> list[CartesianND]:
    """
    Points for the four-body geometry with the relative pair distances
    (1, sqrt(3), sqrt(3), sqrt(3), sqrt(11/3), 2)
    # (1.000000, 1.732051, 1.732051, 1.732051, 1.914854, 2.000000)
    """
    _check_lat_const_positive(lat_const)
    points = [
        (0.000000, 0.000000, 0.000000),
        (0.500000, 0.288675, 0.816497),
        (1.500000, 0.288675, -0.816497),
        (1.000000, 1.732051, 0.000000),
    ]

    return [lat_const * Cartesian3D(*p) for p in points]


def fourbody_geometry_sqrt3_sqrt3_2_2_2(lat_const: float) -> list[CartesianND]:
    """
    Points for the four-body geometry with the relative pair distances
    (1, sqrt(3), sqrt(3), 2, 2, 2)
    # (1.000000, 1.732051, 1.732051, 2.000000, 2.000000, 2.000000)
    """
    _check_lat_const_positive(lat_const)
    points = [
        (0.000000, 0.000000, 0.000000),
        (0.500000, 0.288675, 0.816497),
        (1.000000, 1.732051, 0.000000),
        (2.000000, 0.000000, 0.000000),
    ]

    return [lat_const * Cartesian3D(*p) for p in points]


def fourbody_geometry_sqrt3_sqrt113_sqrt113_sqrt113_sqrt113(
    lat_const: float,
) -> list[CartesianND]:
    """
    Points for the four-body geometry with the relative pair distances
    (1, sqrt(3), sqrt(11/3), sqrt(11/3), sqrt(11/3), sqrt(11/3))
    # (1.000000, 1.732051, 1.914854, 1.914854, 1.914854, 1.914854)
    """
    _check_lat_const_positive(lat_const)
    points = [
        (0.000000, 0.000000, 0.000000),
        (0.500000, 0.866025, 0.000000),
        (1.000000, 0.000000, 1.632993),
        (-0.500000, 0.866025, 1.632993),
    ]

    return [lat_const * Cartesian3D(*p) for p in points]


def fourbody_geometry_sqrt3_sqrt113_sqrt113_sqrt113_2(
    lat_const: float,
) -> list[CartesianND]:
    """
    Points for the four-body geometry with the relative pair distances
    (1, sqrt(3), sqrt(11/3), sqrt(11/3), sqrt(11/3), 2)
    # (1.000000, 1.732051, 1.914854, 1.914854, 1.914854, 2.000000)
    """
    _check_lat_const_positive(lat_const)
    points = [
        (0.000000, 0.000000, 0.000000),
        (0.500000, 0.866025, 0.000000),
        (1.000000, 0.000000, 1.632993),
        (1.500000, -0.866025, 0.000000),
    ]

    return [lat_const * Cartesian3D(*p) for p in points]
