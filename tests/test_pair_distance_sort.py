import itertools
from typing import Sequence
from typing import Tuple

import pytest

from cartesian import CartesianND
from cartesian.measure import euclidean_distance
from hydro4b_coords.sidelength_swap import repeated_index_swap_sort
from hydro4b_coords.geometries import fourbody_geometry_sqrt2_sqrt3_sqrt3_a
from hydro4b_coords.geometries import fourbody_geometry_sqrt2_sqrt3_sqrt3_b


def rounded_tuple_values(values: Sequence[float], n_round: int) -> Tuple[float, ...]:
    return tuple([round(val, n_round) for val in values])


def relative_pair_distances(points: list[CartesianND]) -> list[float]:
    return [euclidean_distance(p0, p1) for p0, p1 in itertools.combinations(points, 2)]


def assert_all_approx_equal(expected: list[float], actual: list[float]) -> None:
    for (exp, act) in zip(expected, actual):
        assert exp == pytest.approx(act)


class Test_index_swap_sort:
    def test_basic_functionality(self):
        lat_const = 1.0
        points0 = fourbody_geometry_sqrt2_sqrt3_sqrt3_a(lat_const)
        points1 = [points0[0], points0[1], points0[3], points0[2]]

        pairdists0 = relative_pair_distances(points0)
        pairdists0 = rounded_tuple_values(pairdists0, 3)
        sorted_pairdists0 = repeated_index_swap_sort(pairdists0)

        pairdists1 = relative_pair_distances(points1)
        pairdists1 = rounded_tuple_values(pairdists1, 3)
        sorted_pairdists1 = repeated_index_swap_sort(pairdists0)

        print(f"pairdists0: {pairdists0}")
        print(f"pairdists1: {pairdists1}")
        print(f"sorted_pairdists0: {sorted_pairdists0}")
        print(f"sorted_pairdists1: {sorted_pairdists1}")

        assert pairdists0 != pairdists1
        assert sorted_pairdists0 == sorted_pairdists1
