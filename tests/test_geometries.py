import itertools
import math

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


class TestEquilateralTriangle:
    def test_equidistant(self):
        lat_const = 1.0
        points = geometries.equilateral_triangle(lat_const)
        distfunc = measure.euclidean_distance
        
        for (pi, pj) in itertools.combinations(points, 2):
            assert measure.distance(pi, pj) == pytest.approx(lat_const)

class TestIrregularTetrahedron:
    @pytest.mark.parametrize('lat_const', [1.0, 0.5, 2.0])
    def test_distances(self, lat_const):
        points = geometries.irregular_tetrahedron(lat_const)
        distfunc = measure.euclidean_distance
    
        pair_distances = sorted([
            distfunc(pi, pj)
            for (pi, pj) in itertools.combinations(points, 2)
        ])
        
        assert len(pair_distances) == 6
        
        # five of the pair distances are equal to the lattice constant; the sixth
        # and longest distance is sqrt(2) * lat_const
        for i_pair in range(5):
            assert pair_distances[i_pair] == pytest.approx(lat_const)
        assert pair_distances[-1] == pytest.approx(lat_const * math.sqrt(2.0))


@pytest.mark.parametrize('lat_const', [-1.0, 0.0])
@pytest.mark.parametrize(
    'point_creating_function',
    [
        geometries.equilateral_triangle,
        geometries.tetrahedron,
        geometries.irregular_tetrahedron,
    ]
)
def test_raises_non_positive(lat_const, point_creating_function):
    with pytest.raises(ValueError) as exc_info:
        point_creating_function(lat_const)
    
    assert (
        f"The lattice constant must be positive. Entered: {lat_const}"
        in str(exc_info.value)
    )

