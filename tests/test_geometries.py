import itertools

import pytest
from cartesian import measure

from hydro4b_coords import geometries


class TestTetrahedron:
    def test_equidistant(self):
        lat_const = 1.0
        points = geometries.tetrahedron(lat_const)
        distfunc = measure.euclidean_distance
        
        for (pi, pj) in itertools.combinations(points, 2):
            assert measure.distance(pi, pj) == pytest.approx(lat_const)
