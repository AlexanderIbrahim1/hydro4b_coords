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


def irregular_tetrahedron(lat_const: float) -> list[CartesianND]:
    _check_lat_const_positive(lat_const)

    # the specific angle that generates the irregular tetrahedron in question
    irregular_tetrahedron_angle = 2.0 * math.asin(math.sqrt(2.0/3.0))
    alpha = math.pi - irregular_tetrahedron_angle

    equil_tri_height = math.sqrt(3.0/4.0)

    y_pos = - equil_tri_height * math.cos(alpha)
    z_pos =   equil_tri_height * math.sin(alpha)

    return [
        lat_const * Cartesian3D(-0.5, 0.0, 0.0),
        lat_const * Cartesian3D(0.5, 0.0, 0.0),
        lat_const * Cartesian3D(0.0, math.sqrt(3.0 / 4.0), 0.0),
        lat_const * Cartesian3D(0.0, y_pos, z_pos),
    ]


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


