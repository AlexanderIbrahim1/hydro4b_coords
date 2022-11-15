"""
This module contains functions that return collections of points for specific
geometries (such as the tetrahedron, etc.).
"""

import math

from cartesian import Cartesian3D
from cartesian import CartesianND


def tetrahedron(lat_const: float) -> list[CartesianND]:
    _check_lat_const_positive(lat_const)

    return [
        lat_const * Cartesian3D(-0.5, 0.0, 0.0),
        lat_const * Cartesian3D(0.5, 0.0, 0.0),
        lat_const * Cartesian3D(0.0, math.sqrt(3.0 / 4.0), 0.0),
        lat_const * Cartesian3D(0.0, math.sqrt(1.0 / 12.0), math.sqrt(2.0 / 3.0)),
    ]


def irregular_tetrahedron(
    lat_const: float, irregular_tetrahedron_angle: float
) -> list[CartesianND]:
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


def irregular_tetrahedron_sqrt2(lat_const: float) -> list[CartesianND]:
    irregular_tetrahedron_angle = 2.0 * math.asin(math.sqrt(2.0 / 3.0))
    return irregular_tetrahedron(lat_const, irregular_tetrahedron_angle)


def irregular_tetrahedron_sqrt83(lat_const: float) -> list[CartesianND]:
    irregular_tetrahedron_angle = 2.0 * math.asin(math.sqrt(8.0 / 9.0))
    return irregular_tetrahedron(lat_const, irregular_tetrahedron_angle)


def irregular_tetrahedron_sqrt3(lat_const: float) -> list[CartesianND]:
    irregular_tetrahedron_angle = 2.0 * math.asin(1.0)
    return irregular_tetrahedron(lat_const, irregular_tetrahedron_angle)


def equilateral_triangle(lat_const: float) -> list[CartesianND]:
    _check_lat_const_positive(lat_const)

    return [
        lat_const * Cartesian3D(-0.5, 0.0, 0.0),
        lat_const * Cartesian3D(0.5, 0.0, 0.0),
        lat_const * Cartesian3D(0.0, math.sqrt(3.0 / 4.0), 0.0),
    ]


def _check_lat_const_positive(lat_const: float) -> None:
    if lat_const <= 0.0:
        raise ValueError(f"The lattice constant must be positive. Entered: {lat_const}")
