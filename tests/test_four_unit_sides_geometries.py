import itertools
import math

import pytest

from cartesian import CartesianND
from cartesian.measure import euclidean_distance

from hydro4b_coords.geometries import fourbody_geometry_sqrt2_sqrt2
from hydro4b_coords.geometries import fourbody_geometry_sqrt2_sqrt3
from hydro4b_coords.geometries import fourbody_geometry_sqrt3_sqrt3
from hydro4b_coords.geometries import fourbody_geometry_sqrt3_2
from hydro4b_coords.geometries import fourbody_geometry_sqrt2_sqrt113
from hydro4b_coords.geometries import fourbody_geometry_sqrt3_sqrt113
from hydro4b_coords.geometries import fourbody_geometry_sqrt83_sqrt113
from hydro4b_coords.geometries import fourbody_geometry_sqrt113_sqrt113


def relative_pair_distances(points: list[CartesianND]) -> list[float]:
    return [euclidean_distance(p0, p1) for p0, p1 in itertools.combinations(points, 2)]


def assert_all_approx_equal(expected: list[float], actual: list[float]) -> None:
    for (exp, act) in zip(expected, actual):
        assert exp == pytest.approx(act)


@pytest.mark.parametrize("lat_const", [1.0, 2.0, 3.0])
def test_fourbody_geometry_sqrt2_sqrt2(lat_const):
    points = fourbody_geometry_sqrt2_sqrt2(lat_const)

    actual_pair_distances = sorted(relative_pair_distances(points))
    expected_pair_distances = [1.0, 1.0, 1.0, 1.0, math.sqrt(2.0), math.sqrt(2.0)]
    expected_pair_distances = [lat_const * pd for pd in expected_pair_distances]

    assert_all_approx_equal(actual_pair_distances, expected_pair_distances)


@pytest.mark.parametrize("lat_const", [1.0, 2.0, 3.0])
def test_fourbody_geometry_sqrt2_sqrt3(lat_const):
    points = fourbody_geometry_sqrt2_sqrt3(lat_const)

    actual_pair_distances = sorted(relative_pair_distances(points))
    expected_pair_distances = [1.0, 1.0, 1.0, 1.0, math.sqrt(2.0), math.sqrt(3.0)]
    expected_pair_distances = [lat_const * pd for pd in expected_pair_distances]

    assert_all_approx_equal(actual_pair_distances, expected_pair_distances)


@pytest.mark.parametrize("lat_const", [1.0, 2.0, 3.0])
def test_fourbody_geometry_sqrt3_sqrt3(lat_const):
    points = fourbody_geometry_sqrt3_sqrt3(lat_const)

    actual_pair_distances = sorted(relative_pair_distances(points))
    expected_pair_distances = [1.0, 1.0, 1.0, 1.0, math.sqrt(3.0), math.sqrt(3.0)]
    expected_pair_distances = [lat_const * pd for pd in expected_pair_distances]

    assert_all_approx_equal(actual_pair_distances, expected_pair_distances)


@pytest.mark.parametrize("lat_const", [1.0, 2.0, 3.0])
def test_fourbody_geometry_sqrt3_2(lat_const):
    points = fourbody_geometry_sqrt3_2(lat_const)

    actual_pair_distances = sorted(relative_pair_distances(points))
    expected_pair_distances = [1.0, 1.0, 1.0, 1.0, math.sqrt(3.0), 2.0]
    expected_pair_distances = [lat_const * pd for pd in expected_pair_distances]

    assert_all_approx_equal(actual_pair_distances, expected_pair_distances)


@pytest.mark.parametrize("lat_const", [1.0, 2.0, 3.0])
def test_fourbody_geometry_sqrt2_sqrt113(lat_const):
    points = fourbody_geometry_sqrt2_sqrt113(lat_const)

    actual_pair_distances = sorted(relative_pair_distances(points))
    expected_pair_distances = [
        1.0,
        1.0,
        1.0,
        1.0,
        math.sqrt(2.0),
        math.sqrt(11.0 / 3.0),
    ]
    expected_pair_distances = [lat_const * pd for pd in expected_pair_distances]

    assert_all_approx_equal(actual_pair_distances, expected_pair_distances)


@pytest.mark.parametrize("lat_const", [1.0, 2.0, 3.0])
def test_fourbody_geometry_sqrt3_sqrt113(lat_const):
    points = fourbody_geometry_sqrt3_sqrt113(lat_const)

    actual_pair_distances = sorted(relative_pair_distances(points))
    expected_pair_distances = [
        1.0,
        1.0,
        1.0,
        1.0,
        math.sqrt(3.0),
        math.sqrt(11.0 / 3.0),
    ]
    expected_pair_distances = [lat_const * pd for pd in expected_pair_distances]

    assert_all_approx_equal(actual_pair_distances, expected_pair_distances)


@pytest.mark.parametrize("lat_const", [1.0, 2.0, 3.0])
def test_fourbody_geometry_sqrt83_sqrt113(lat_const):
    points = fourbody_geometry_sqrt83_sqrt113(lat_const)

    actual_pair_distances = sorted(relative_pair_distances(points))
    expected_pair_distances = [
        1.0,
        1.0,
        1.0,
        1.0,
        math.sqrt(8.0 / 3.0),
        math.sqrt(11.0 / 3.0),
    ]
    expected_pair_distances = [lat_const * pd for pd in expected_pair_distances]

    assert_all_approx_equal(actual_pair_distances, expected_pair_distances)


@pytest.mark.parametrize("lat_const", [1.0, 2.0, 3.0])
def test_fourbody_geometry_sqrt113_sqrt113(lat_const):
    points = fourbody_geometry_sqrt113_sqrt113(lat_const)

    actual_pair_distances = sorted(relative_pair_distances(points))
    expected_pair_distances = [
        1.0,
        1.0,
        1.0,
        1.0,
        math.sqrt(11.0 / 3.0),
        math.sqrt(11.0 / 3.0),
    ]
    expected_pair_distances = [lat_const * pd for pd in expected_pair_distances]

    assert_all_approx_equal(actual_pair_distances, expected_pair_distances)
