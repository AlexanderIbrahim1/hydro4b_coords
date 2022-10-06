"""
This module contains functions that return collections of points for specific
geometries (such as the tetrahedron, etc.).
"""

import math

from cartesian import Cartesian3D
from cartesian import CartesianND


def tetrahedron(lat_const: float) -> list[CartesianND]:
    return [
        lat_const * Cartesian3D(-0.5, 0.0, 0.0),
        lat_const * Cartesian3D(0.5, 0.0, 0.0),
        lat_const * Cartesian3D(0.0, math.sqrt(3.0 / 4.0), 0.0),
        lat_const * Cartesian3D(0.0, math.sqrt(1.0 / 12.0), math.sqrt(2.0 / 3.0)),
    ]


def equilateral_triangle(lat_const: float) -> list[CartesianND]:
    return [
        lat_const * Cartesian3D(-0.5, 0.0, 0.0),
        lat_const * Cartesian3D(0.5, 0.0, 0.0),
        lat_const * Cartesian3D(0.0, math.sqrt(3.0 / 4.0), 0.0),
    ]
