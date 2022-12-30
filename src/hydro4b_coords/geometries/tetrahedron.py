"""
This module contains a single function, that which return the collection of points
for the tetrahedron.
"""

import math

from cartesian import Cartesian3D
from cartesian import CartesianND

from hydro4b_coords.geometries.checker import _check_lat_const_positive


def tetrahedron(lat_const: float) -> list[CartesianND]:
    _check_lat_const_positive(lat_const)

    return [
        lat_const * Cartesian3D(-0.5, 0.0, 0.0),
        lat_const * Cartesian3D(0.5, 0.0, 0.0),
        lat_const * Cartesian3D(0.0, math.sqrt(3.0 / 4.0), 0.0),
        lat_const * Cartesian3D(0.0, math.sqrt(1.0 / 12.0), math.sqrt(2.0 / 3.0)),
    ]
