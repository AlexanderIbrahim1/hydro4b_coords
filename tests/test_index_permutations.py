import itertools
from typing import Sequence
from typing import Tuple

import pytest

from cartesian import CartesianND
from cartesian.measure import euclidean_distance
from hydro4b_coords.sidelength_swap import LessThanEpsilon
from hydro4b_coords.sidelength_swap import minimum_permutation
from hydro4b_coords.geometries import fourbody_geometry_sqrt2_sqrt3_sqrt3_a
from hydro4b_coords.geometries import fourbody_geometry_sqrt2_sqrt3_sqrt3_b


def relative_pair_distances(points: list[CartesianND]) -> list[float]:
    return [euclidean_distance(p0, p1) for p0, p1 in itertools.combinations(points, 2)]


def all_approx_equal(expected: list[float], actual: list[float]) -> None:
    return all([exp == pytest.approx(act) for (exp, act) in zip(expected, actual)])


class Test_minium_permutation:
    def test_basic_functionality(self):
        lat_const = 1.0
        points0 = fourbody_geometry_sqrt2_sqrt3_sqrt3_a(lat_const)
        points1 = [points0[0], points0[1], points0[3], points0[2]]

        pairdists0 = relative_pair_distances(points0)
        pairdists1 = relative_pair_distances(points1)

        less_than_comparator = LessThanEpsilon(1.0e-4)
        sorted_pairdists0 = minimum_permutation(pairdists0, less_than_comparator)
        sorted_pairdists1 = minimum_permutation(pairdists1, less_than_comparator)

        assert not all_approx_equal(pairdists0, pairdists1)
        assert all_approx_equal(sorted_pairdists0, sorted_pairdists1)
