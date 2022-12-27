import itertools
import math

import pytest

from cartesian import CartesianND
from cartesian.measure import euclidean_distance

from hydro4b_coords.geometries import fourbody_geometry_sqrt2_sqrt2_sqrt83_sqrt3
from hydro4b_coords.geometries import fourbody_geometry_sqrt2_sqrt2_sqrt83_sqrt113
from hydro4b_coords.geometries import fourbody_geometry_sqrt2_sqrt2_sqrt3_sqrt3_a
from hydro4b_coords.geometries import fourbody_geometry_sqrt2_sqrt2_sqrt3_sqrt3_b
from hydro4b_coords.geometries import fourbody_geometry_sqrt2_sqrt2_sqrt3_2
from hydro4b_coords.geometries import fourbody_geometry_sqrt2_sqrt3_sqrt3_sqrt3
from hydro4b_coords.geometries import fourbody_geometry_sqrt2_sqrt3_sqrt3_sqrt113_a
from hydro4b_coords.geometries import fourbody_geometry_sqrt2_sqrt3_sqrt3_sqrt113_b
from hydro4b_coords.geometries import fourbody_geometry_sqrt2_sqrt3_sqrt3_sqrt113_c
from hydro4b_coords.geometries import fourbody_geometry_sqrt2_sqrt3_sqrt3_2_a
from hydro4b_coords.geometries import fourbody_geometry_sqrt2_sqrt3_sqrt3_2_b
from hydro4b_coords.geometries import fourbody_geometry_sqrt2_sqrt3_sqrt3_2_c
from hydro4b_coords.geometries import fourbody_geometry_sqrt2_sqrt3_sqrt113_sqrt113_a
from hydro4b_coords.geometries import fourbody_geometry_sqrt2_sqrt3_sqrt113_sqrt113_b
from hydro4b_coords.geometries import fourbody_geometry_sqrt2_sqrt3_sqrt113_sqrt113_c
from hydro4b_coords.geometries import fourbody_geometry_sqrt2_sqrt3_sqrt113_sqrt113_d
from hydro4b_coords.geometries import fourbody_geometry_sqrt83_sqrt83_sqrt113_sqrt113
from hydro4b_coords.geometries import fourbody_geometry_sqrt83_sqrt3_sqrt3_sqrt3
from hydro4b_coords.geometries import fourbody_geometry_sqrt83_sqrt3_sqrt3_sqrt113
from hydro4b_coords.geometries import fourbody_geometry_sqrt83_sqrt3_sqrt3_2
from hydro4b_coords.geometries import fourbody_geometry_sqrt83_sqrt3_sqrt113_sqrt113
from hydro4b_coords.geometries import fourbody_geometry_sqrt83_sqrt113_sqrt113_sqrt113
from hydro4b_coords.geometries import fourbody_geometry_sqrt83_sqrt113_sqrt113_2
from hydro4b_coords.geometries import fourbody_geometry_sqrt3_sqrt3_sqrt3_sqrt113
from hydro4b_coords.geometries import fourbody_geometry_sqrt3_sqrt3_sqrt3_2_a
from hydro4b_coords.geometries import fourbody_geometry_sqrt3_sqrt3_sqrt3_2_b
from hydro4b_coords.geometries import fourbody_geometry_sqrt3_sqrt3_sqrt3_2_c
from hydro4b_coords.geometries import fourbody_geometry_sqrt3_sqrt3_sqrt113_sqrt113_a
from hydro4b_coords.geometries import fourbody_geometry_sqrt3_sqrt3_sqrt113_sqrt113_b
from hydro4b_coords.geometries import fourbody_geometry_sqrt3_sqrt3_sqrt113_sqrt113_c
from hydro4b_coords.geometries import fourbody_geometry_sqrt3_sqrt3_sqrt113_2
from hydro4b_coords.geometries import fourbody_geometry_sqrt3_sqrt3_2_2
from hydro4b_coords.geometries import fourbody_geometry_sqrt3_sqrt113_sqrt113_sqrt113
from hydro4b_coords.geometries import fourbody_geometry_sqrt3_sqrt113_sqrt113_2
from hydro4b_coords.geometries import fourbody_geometry_sqrt3_2_2_2                 

MAP_KEY_TO_FUNCTION = {
    'sqrt2_sqrt2_sqrt83_sqrt3'         : fourbody_geometry_sqrt2_sqrt2_sqrt83_sqrt3,
    'sqrt2_sqrt2_sqrt83_sqrt113'       : fourbody_geometry_sqrt2_sqrt2_sqrt83_sqrt113,
    'sqrt2_sqrt2_sqrt3_sqrt3_a'        : fourbody_geometry_sqrt2_sqrt2_sqrt3_sqrt3_a,
    'sqrt2_sqrt2_sqrt3_sqrt3_b'        : fourbody_geometry_sqrt2_sqrt2_sqrt3_sqrt3_b,
    'sqrt2_sqrt2_sqrt3_2'              : fourbody_geometry_sqrt2_sqrt2_sqrt3_2,
    'sqrt2_sqrt3_sqrt3_sqrt3'          : fourbody_geometry_sqrt2_sqrt3_sqrt3_sqrt3,
    'sqrt2_sqrt3_sqrt3_sqrt113_a'      : fourbody_geometry_sqrt2_sqrt3_sqrt3_sqrt113_a,
    'sqrt2_sqrt3_sqrt3_sqrt113_b'      : fourbody_geometry_sqrt2_sqrt3_sqrt3_sqrt113_b,
    'sqrt2_sqrt3_sqrt3_sqrt113_c'      : fourbody_geometry_sqrt2_sqrt3_sqrt3_sqrt113_c,
    'sqrt2_sqrt3_sqrt3_2_a'            : fourbody_geometry_sqrt2_sqrt3_sqrt3_2_a,
    'sqrt2_sqrt3_sqrt3_2_b'            : fourbody_geometry_sqrt2_sqrt3_sqrt3_2_b,
    'sqrt2_sqrt3_sqrt3_2_c'            : fourbody_geometry_sqrt2_sqrt3_sqrt3_2_c,
    'sqrt2_sqrt3_sqrt113_sqrt113_a'    : fourbody_geometry_sqrt2_sqrt3_sqrt113_sqrt113_a,
    'sqrt2_sqrt3_sqrt113_sqrt113_b'    : fourbody_geometry_sqrt2_sqrt3_sqrt113_sqrt113_b,
    'sqrt2_sqrt3_sqrt113_sqrt113_c'    : fourbody_geometry_sqrt2_sqrt3_sqrt113_sqrt113_c,
    'sqrt2_sqrt3_sqrt113_sqrt113_d'    : fourbody_geometry_sqrt2_sqrt3_sqrt113_sqrt113_d,
    'sqrt83_sqrt83_sqrt113_sqrt113'    : fourbody_geometry_sqrt83_sqrt83_sqrt113_sqrt113,
    'sqrt83_sqrt3_sqrt3_sqrt3'         : fourbody_geometry_sqrt83_sqrt3_sqrt3_sqrt3,
    'sqrt83_sqrt3_sqrt3_sqrt113'       : fourbody_geometry_sqrt83_sqrt3_sqrt3_sqrt113,
    'sqrt83_sqrt3_sqrt3_2'             : fourbody_geometry_sqrt83_sqrt3_sqrt3_2,
    'sqrt83_sqrt3_sqrt113_sqrt113'     : fourbody_geometry_sqrt83_sqrt3_sqrt113_sqrt113,
    'sqrt83_sqrt113_sqrt113_sqrt113'   : fourbody_geometry_sqrt83_sqrt113_sqrt113_sqrt113,
    'sqrt83_sqrt113_sqrt113_2'         : fourbody_geometry_sqrt83_sqrt113_sqrt113_2,
    'sqrt3_sqrt3_sqrt3_sqrt113'        : fourbody_geometry_sqrt3_sqrt3_sqrt3_sqrt113,
    'sqrt3_sqrt3_sqrt3_2_a'            : fourbody_geometry_sqrt3_sqrt3_sqrt3_2_a,
    'sqrt3_sqrt3_sqrt3_2_b'            : fourbody_geometry_sqrt3_sqrt3_sqrt3_2_b,
    'sqrt3_sqrt3_sqrt3_2_c'            : fourbody_geometry_sqrt3_sqrt3_sqrt3_2_c,
    'sqrt3_sqrt3_sqrt113_sqrt113_a'    : fourbody_geometry_sqrt3_sqrt3_sqrt113_sqrt113_a,
    'sqrt3_sqrt3_sqrt113_sqrt113_b'    : fourbody_geometry_sqrt3_sqrt3_sqrt113_sqrt113_b,
    'sqrt3_sqrt3_sqrt113_sqrt113_c'    : fourbody_geometry_sqrt3_sqrt3_sqrt113_sqrt113_c,
    'sqrt3_sqrt3_sqrt113_2'            : fourbody_geometry_sqrt3_sqrt3_sqrt113_2,
    'sqrt3_sqrt3_2_2'                  : fourbody_geometry_sqrt3_sqrt3_2_2,
    'sqrt3_sqrt113_sqrt113_sqrt113'    : fourbody_geometry_sqrt3_sqrt113_sqrt113_sqrt113,
    'sqrt3_sqrt113_sqrt113_2'          : fourbody_geometry_sqrt3_sqrt113_sqrt113_2,
    'sqrt3_2_2_2'                      : fourbody_geometry_sqrt3_2_2_2,
}

def sidelengths_from_geometry_tag(geometry_tag: str) -> list[float]:
    map_token_to_sidelength = {
        'sqrt2': math.sqrt(2.0),
        'sqrt83': math.sqrt(8.0/3.0),
        'sqrt3': math.sqrt(3.0),
        'sqrt113': math.sqrt(11.0/3.0),
        '2': 2.0,
    }
    
    tag_delimiter = '_'
    tokens = geometry_tag.split(tag_delimiter)
    starting_sidelengths = [1.0, 1.0]
    ending_sidelengths = [
        map_token_to_sidelength[token]
        for token in tokens[:4]
    ]
        
    return starting_sidelengths + ending_sidelengths
    

def relative_pair_distances(points: list[CartesianND]) -> list[float]:
    return [euclidean_distance(p0, p1) for p0, p1 in itertools.combinations(points, 2)]


def assert_all_approx_equal(expected: list[float], actual: list[float]) -> None:
    for (exp, act) in zip(expected, actual):
        assert exp == pytest.approx(act)

@pytest.mark.parametrize("lat_const", [1.0, 2.0, 3.0])
@pytest.mark.parametrize("geometry_tag", list(MAP_KEY_TO_FUNCTION.keys()))
def test_fourbody_geometry(lat_const, geometry_tag):
    function = MAP_KEY_TO_FUNCTION[geometry_tag]
    points = function(lat_const)
    actual_pair_distances = sorted(relative_pair_distances(points))

    unscaled_pair_distances = sidelengths_from_geometry_tag(geometry_tag)
    expected_pair_distances = [
        lat_const * pd for pd in unscaled_pair_distances
    ]

    assert_all_approx_equal(actual_pair_distances, expected_pair_distances)

