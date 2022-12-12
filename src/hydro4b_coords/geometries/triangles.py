"""
This module contains functions that return collections of points for specific
three-body (triangle) geometries.

Right now there is only the equilateral triangle, as I have not needed any other
geometries yet.
"""

import math

from cartesian import Cartesian3D
from cartesian import CartesianND

from hydro4b_coords.geometries.checker import _check_lat_const_positive


def equilateral_triangle(lat_const: float) -> list[CartesianND]:
    _check_lat_const_positive(lat_const)

    return [
        lat_const * Cartesian3D(-0.5, 0.0, 0.0),
        lat_const * Cartesian3D(0.5, 0.0, 0.0),
        lat_const * Cartesian3D(0.0, math.sqrt(3.0 / 4.0), 0.0),
    ]
