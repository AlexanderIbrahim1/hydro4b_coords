import itertools
import math

import pytest

from cartesian import CartesianND
from cartesian.measure import euclidean_distance

from hydro4b_coords.geometries import MAP_GEOMETRY_TAG_TO_FUNCTION

MAP_TOKEN_TO_SIDELENGTH = {
    "sqrt2": math.sqrt(2.0),
    "sqrt83": math.sqrt(8.0 / 3.0),
    "sqrt3": math.sqrt(3.0),
    "sqrt113": math.sqrt(11.0 / 3.0),
    "2": 2.0,
}


def get_ending_sidelengths(geometry_tag: str) -> list[float]:
    """
    Get the 'ending' sidelengths of a four-body geometry, which are the sidelengths
    longer than the lattice constant.

    For example, if all six sidelengths (sorted) of a certain geometry are

        (1, 1, 1, sqrt(2), sqrt(3), sqrt(11/3))

    return [sqrt(2), sqrt(3), sqrt(11/3)]
    """
    valid_tokens = list(MAP_TOKEN_TO_SIDELENGTH.keys())

    tag_delimiter = "_"
    tokens = geometry_tag.split(tag_delimiter)
    ending_sidelengths = [
        MAP_TOKEN_TO_SIDELENGTH[token] for token in tokens if token in valid_tokens
    ]

    return ending_sidelengths


def get_starting_sidelengths(n_ending_sidelengths: int) -> list[float]:
    """
    Get the sidelengths of a geometry corresponding to the lattice constant.

    For example, if all six sidelengths (sorted) of a certain geometry are

        (1, 1, 1, sqrt(2), sqrt(3), sqrt(11/3))

    return [1, 1, 1]
    """
    assert 0 <= n_ending_sidelengths < 6

    n_total_sidelengths = 6
    n_starting_sidelengths = n_total_sidelengths - n_ending_sidelengths

    return [1.0] * n_starting_sidelengths


def sidelengths_from_geometry_tag(geometry_tag: str) -> list[float]:
    tetrahedron_tag = "1"
    if geometry_tag == tetrahedron_tag:
        return [1.0] * 6

    ending_sidelengths = get_ending_sidelengths(geometry_tag)
    starting_sidelengths = get_starting_sidelengths(len(ending_sidelengths))

    return starting_sidelengths + ending_sidelengths


def relative_pair_distances(points: list[CartesianND]) -> list[float]:
    return [euclidean_distance(p0, p1) for p0, p1 in itertools.combinations(points, 2)]


def assert_all_approx_equal(expected: list[float], actual: list[float]) -> None:
    for (exp, act) in zip(expected, actual):
        assert exp == pytest.approx(act)


@pytest.mark.parametrize("lat_const", [1.0, 2.0, 3.0])
@pytest.mark.parametrize("geometry_tag", list(MAP_GEOMETRY_TAG_TO_FUNCTION.keys()))
def test_geometry_side_lengths(lat_const, geometry_tag):
    """
    Generate the points for a four-body geometry given its geometry tag, calculate
    all the relative side lengths of the geometry, and make sure they correspond
    to the expected side lengths.
    """
    function = MAP_GEOMETRY_TAG_TO_FUNCTION[geometry_tag]
    points = function(lat_const)
    actual_pair_distances = sorted(relative_pair_distances(points))

    unscaled_pair_distances = sidelengths_from_geometry_tag(geometry_tag)
    expected_pair_distances = [lat_const * pd for pd in unscaled_pair_distances]

    assert_all_approx_equal(actual_pair_distances, expected_pair_distances)
