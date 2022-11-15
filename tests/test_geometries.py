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
    def test_correct_number_of_points(self):
        lat_const = 1.0
        angle_rad = 90.0

        points = geometries.irregular_tetrahedron(lat_const, angle_rad)
        pair_distances = [
            measure.euclidean_distance(pi, pj)
            for (pi, pj) in itertools.combinations(points, 2)
        ]
        assert len(points) == 4
        assert len(pair_distances) == 6

    @pytest.mark.parametrize("lat_const", [1.0, 0.5, 2.0])
    @pytest.mark.parametrize("angle_deg", [70.6, 90.0, 145.0, 180.0])
    def test_basic_properties_large_angle(self, lat_const, angle_deg):
        """
        For angles between 'math.acos(1.0/3.0)' and '180.0', five of the pair
        distances should be equal to the lattice constant, and the last should
        be longer than the others.
        """
        angle_rad = (math.pi / 180.0) * angle_deg
        distfunc = measure.euclidean_distance

        points = geometries.irregular_tetrahedron(lat_const, angle_rad)
        pair_distances = sorted(
            [distfunc(pi, pj) for (pi, pj) in itertools.combinations(points, 2)]
        )

        # five of the pair distances are equal to the lattice constant
        for i_pair in range(5):
            assert pair_distances[i_pair] == pytest.approx(lat_const)

        # the sixth distance is found using the cosine triangle identity
        last_side_length = self.irregular_tetrahedron_last_side_length(
            lat_const, angle_rad
        )
        assert pair_distances[-1] == pytest.approx(last_side_length)
        assert pair_distances[-1] > lat_const

    @pytest.mark.parametrize("lat_const", [1.0, 0.5, 2.0])
    @pytest.mark.parametrize("angle_deg", [0.0, 10.0, 20.0, 50.0, 70.4])
    def test_basic_properties_small_angle(self, lat_const, angle_deg):
        """
        For angles between '0.0' and 'math.acos(1.0/3.0)', five of the pair
        distances should be equal to the lattice constant, and the last should
        be shorter than the others.
        """
        angle_rad = (math.pi / 180.0) * angle_deg
        distfunc = measure.euclidean_distance

        points = geometries.irregular_tetrahedron(lat_const, angle_rad)
        pair_distances = sorted(
            [distfunc(pi, pj) for (pi, pj) in itertools.combinations(points, 2)]
        )

        # five of the pair distances are equal to the lattice constant
        for i_pair in range(1, 6):
            assert pair_distances[i_pair] == pytest.approx(lat_const)

        # the sixth distance is found using the cosine triangle identity
        last_side_length = self.irregular_tetrahedron_last_side_length(
            lat_const, angle_rad
        )
        assert pair_distances[0] == pytest.approx(last_side_length)
        assert pair_distances[0] < lat_const

    def irregular_tetrahedron_last_side_length(
        self, lat_const: float, angle_rad: float
    ) -> float:
        height_of_eq_tri = math.sqrt(3.0 / 4.0) * lat_const
        return math.sqrt(2.0 * (1.0 - math.cos(angle_rad))) * height_of_eq_tri


class TestIrregularTetrahedronSpecial:
    @pytest.mark.parametrize("lat_const", [1.0, 0.5, 2.0])
    @pytest.mark.parametrize(
        "point_creating_function, long_side_len_ratio",
        [
            (geometries.irregular_tetrahedron_sqrt2, math.sqrt(2.0)),
            (geometries.irregular_tetrahedron_sqrt83, math.sqrt(8.0 / 3.0)),
            (geometries.irregular_tetrahedron_sqrt3, math.sqrt(3.0)),
        ],
    )
    def test_distances(self, lat_const, point_creating_function, long_side_len_ratio):
        points = point_creating_function(lat_const)
        distfunc = measure.euclidean_distance

        pair_distances = sorted(
            [distfunc(pi, pj) for (pi, pj) in itertools.combinations(points, 2)]
        )

        assert len(pair_distances) == 6

        # five of the pair distances are equal to the lattice constant; the sixth
        # and longest distance is long_side_len_ratio * lat_const
        for i_pair in range(5):
            assert pair_distances[i_pair] == pytest.approx(lat_const)
        assert pair_distances[-1] == pytest.approx(lat_const * long_side_len_ratio)


@pytest.mark.parametrize("lat_const", [-1.0, 0.0])
@pytest.mark.parametrize(
    "point_creating_function",
    [
        geometries.equilateral_triangle,
        geometries.tetrahedron,
        geometries.irregular_tetrahedron_sqrt2,
    ],
)
def test_raises_non_positive(lat_const, point_creating_function):
    with pytest.raises(ValueError) as exc_info:
        point_creating_function(lat_const)

    assert f"The lattice constant must be positive. Entered: {lat_const}" in str(
        exc_info.value
    )
