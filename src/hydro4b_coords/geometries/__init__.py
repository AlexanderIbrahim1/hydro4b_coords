# fmt: off
from hydro4b_coords.geometries.triangles import equilateral_triangle

from hydro4b_coords.geometries.tetrahedron import tetrahedron

from hydro4b_coords.geometries.five_unit_sides import fourbody_geometry_sqrt2
from hydro4b_coords.geometries.five_unit_sides import fourbody_geometry_sqrt83
from hydro4b_coords.geometries.five_unit_sides import fourbody_geometry_sqrt3

# old names to keep the previous function calls working
from hydro4b_coords.geometries.five_unit_sides import irregular_tetrahedron
from hydro4b_coords.geometries.five_unit_sides import irregular_tetrahedron_sqrt2
from hydro4b_coords.geometries.five_unit_sides import irregular_tetrahedron_sqrt3
from hydro4b_coords.geometries.five_unit_sides import irregular_tetrahedron_sqrt83


from hydro4b_coords.geometries.four_unit_sides import fourbody_geometry_sqrt2_sqrt2
from hydro4b_coords.geometries.four_unit_sides import fourbody_geometry_sqrt2_sqrt3
from hydro4b_coords.geometries.four_unit_sides import fourbody_geometry_sqrt3_sqrt3
from hydro4b_coords.geometries.four_unit_sides import fourbody_geometry_sqrt3_2
from hydro4b_coords.geometries.four_unit_sides import fourbody_geometry_sqrt2_sqrt113
from hydro4b_coords.geometries.four_unit_sides import fourbody_geometry_sqrt3_sqrt113
from hydro4b_coords.geometries.four_unit_sides import fourbody_geometry_sqrt83_sqrt113
from hydro4b_coords.geometries.four_unit_sides import fourbody_geometry_sqrt113_sqrt113

from hydro4b_coords.geometries.three_unit_sides import fourbody_geometry_sqrt2_sqrt2_sqrt83
from hydro4b_coords.geometries.three_unit_sides import fourbody_geometry_sqrt2_sqrt2_sqrt113
from hydro4b_coords.geometries.three_unit_sides import fourbody_geometry_sqrt2_sqrt2_2
from hydro4b_coords.geometries.three_unit_sides import fourbody_geometry_sqrt2_sqrt83_sqrt113
from hydro4b_coords.geometries.three_unit_sides import fourbody_geometry_sqrt2_sqrt3_sqrt3_a
from hydro4b_coords.geometries.three_unit_sides import fourbody_geometry_sqrt2_sqrt3_sqrt3_b
from hydro4b_coords.geometries.three_unit_sides import fourbody_geometry_sqrt2_sqrt3_sqrt113_a
from hydro4b_coords.geometries.three_unit_sides import fourbody_geometry_sqrt2_sqrt3_sqrt113_b
from hydro4b_coords.geometries.three_unit_sides import fourbody_geometry_sqrt2_sqrt113_sqrt113_a
from hydro4b_coords.geometries.three_unit_sides import fourbody_geometry_sqrt2_sqrt113_sqrt113_b
from hydro4b_coords.geometries.three_unit_sides import fourbody_geometry_sqrt83_sqrt3_sqrt3
from hydro4b_coords.geometries.three_unit_sides import fourbody_geometry_sqrt83_sqrt3_sqrt113
from hydro4b_coords.geometries.three_unit_sides import fourbody_geometry_sqrt83_sqrt113_sqrt113
from hydro4b_coords.geometries.three_unit_sides import fourbody_geometry_sqrt3_sqrt3_sqrt3_a
from hydro4b_coords.geometries.three_unit_sides import fourbody_geometry_sqrt3_sqrt3_sqrt3_b
from hydro4b_coords.geometries.three_unit_sides import fourbody_geometry_sqrt3_sqrt3_2_a
from hydro4b_coords.geometries.three_unit_sides import fourbody_geometry_sqrt3_sqrt3_2_b

from hydro4b_coords.geometries.two_unit_sides import fourbody_geometry_sqrt2_sqrt2_sqrt83_sqrt3
from hydro4b_coords.geometries.two_unit_sides import fourbody_geometry_sqrt2_sqrt2_sqrt83_sqrt113
from hydro4b_coords.geometries.two_unit_sides import fourbody_geometry_sqrt2_sqrt2_sqrt3_sqrt3_a
from hydro4b_coords.geometries.two_unit_sides import fourbody_geometry_sqrt2_sqrt2_sqrt3_sqrt3_b
from hydro4b_coords.geometries.two_unit_sides import fourbody_geometry_sqrt2_sqrt2_sqrt3_2
from hydro4b_coords.geometries.two_unit_sides import fourbody_geometry_sqrt2_sqrt3_sqrt3_sqrt3
from hydro4b_coords.geometries.two_unit_sides import fourbody_geometry_sqrt2_sqrt3_sqrt3_sqrt113_a
from hydro4b_coords.geometries.two_unit_sides import fourbody_geometry_sqrt2_sqrt3_sqrt3_sqrt113_b
from hydro4b_coords.geometries.two_unit_sides import fourbody_geometry_sqrt2_sqrt3_sqrt3_sqrt113_c
from hydro4b_coords.geometries.two_unit_sides import fourbody_geometry_sqrt2_sqrt3_sqrt3_2_a
from hydro4b_coords.geometries.two_unit_sides import fourbody_geometry_sqrt2_sqrt3_sqrt3_2_b
from hydro4b_coords.geometries.two_unit_sides import fourbody_geometry_sqrt2_sqrt3_sqrt3_2_c
from hydro4b_coords.geometries.two_unit_sides import fourbody_geometry_sqrt2_sqrt3_sqrt113_sqrt113_a
from hydro4b_coords.geometries.two_unit_sides import fourbody_geometry_sqrt2_sqrt3_sqrt113_sqrt113_b
from hydro4b_coords.geometries.two_unit_sides import fourbody_geometry_sqrt2_sqrt3_sqrt113_sqrt113_c
from hydro4b_coords.geometries.two_unit_sides import fourbody_geometry_sqrt2_sqrt3_sqrt113_sqrt113_d
from hydro4b_coords.geometries.two_unit_sides import fourbody_geometry_sqrt83_sqrt83_sqrt113_sqrt113
from hydro4b_coords.geometries.two_unit_sides import fourbody_geometry_sqrt83_sqrt3_sqrt3_sqrt3
from hydro4b_coords.geometries.two_unit_sides import fourbody_geometry_sqrt83_sqrt3_sqrt3_sqrt113
from hydro4b_coords.geometries.two_unit_sides import fourbody_geometry_sqrt83_sqrt3_sqrt3_2
from hydro4b_coords.geometries.two_unit_sides import fourbody_geometry_sqrt83_sqrt3_sqrt113_sqrt113
from hydro4b_coords.geometries.two_unit_sides import fourbody_geometry_sqrt83_sqrt113_sqrt113_sqrt113
from hydro4b_coords.geometries.two_unit_sides import fourbody_geometry_sqrt83_sqrt113_sqrt113_2
from hydro4b_coords.geometries.two_unit_sides import fourbody_geometry_sqrt3_sqrt3_sqrt3_sqrt113
from hydro4b_coords.geometries.two_unit_sides import fourbody_geometry_sqrt3_sqrt3_sqrt3_2_a
from hydro4b_coords.geometries.two_unit_sides import fourbody_geometry_sqrt3_sqrt3_sqrt3_2_b
from hydro4b_coords.geometries.two_unit_sides import fourbody_geometry_sqrt3_sqrt3_sqrt3_2_c
from hydro4b_coords.geometries.two_unit_sides import fourbody_geometry_sqrt3_sqrt3_sqrt113_sqrt113_a
from hydro4b_coords.geometries.two_unit_sides import fourbody_geometry_sqrt3_sqrt3_sqrt113_sqrt113_b
from hydro4b_coords.geometries.two_unit_sides import fourbody_geometry_sqrt3_sqrt3_sqrt113_sqrt113_c
from hydro4b_coords.geometries.two_unit_sides import fourbody_geometry_sqrt3_sqrt3_sqrt113_2
from hydro4b_coords.geometries.two_unit_sides import fourbody_geometry_sqrt3_sqrt3_2_2
from hydro4b_coords.geometries.two_unit_sides import fourbody_geometry_sqrt3_sqrt113_sqrt113_sqrt113
from hydro4b_coords.geometries.two_unit_sides import fourbody_geometry_sqrt3_sqrt113_sqrt113_2
from hydro4b_coords.geometries.two_unit_sides import fourbody_geometry_sqrt3_2_2_2

from hydro4b_coords.geometries.one_unit_side import fourbody_geometry_sqrt2_sqrt2_sqrt83_sqrt3_sqrt3
from hydro4b_coords.geometries.one_unit_side import fourbody_geometry_sqrt2_sqrt2_sqrt83_sqrt3_sqrt113
from hydro4b_coords.geometries.one_unit_side import fourbody_geometry_sqrt2_sqrt2_sqrt3_sqrt3_sqrt113_a
from hydro4b_coords.geometries.one_unit_side import fourbody_geometry_sqrt2_sqrt2_sqrt3_sqrt3_sqrt113_b
from hydro4b_coords.geometries.one_unit_side import fourbody_geometry_sqrt2_sqrt2_sqrt3_sqrt3_2
from hydro4b_coords.geometries.one_unit_side import fourbody_geometry_sqrt2_sqrt2_sqrt3_sqrt113_2
from hydro4b_coords.geometries.one_unit_side import fourbody_geometry_sqrt2_sqrt2_sqrt113_sqrt113_2
from hydro4b_coords.geometries.one_unit_side import fourbody_geometry_sqrt2_sqrt83_sqrt3_sqrt3_sqrt113
from hydro4b_coords.geometries.one_unit_side import fourbody_geometry_sqrt2_sqrt3_sqrt3_sqrt3_sqrt3_a
from hydro4b_coords.geometries.one_unit_side import fourbody_geometry_sqrt2_sqrt3_sqrt3_sqrt3_sqrt3_b
from hydro4b_coords.geometries.one_unit_side import fourbody_geometry_sqrt2_sqrt3_sqrt3_sqrt3_sqrt113
from hydro4b_coords.geometries.one_unit_side import fourbody_geometry_sqrt2_sqrt3_sqrt3_sqrt113_sqrt113_a
from hydro4b_coords.geometries.one_unit_side import fourbody_geometry_sqrt2_sqrt3_sqrt3_sqrt113_sqrt113_b
from hydro4b_coords.geometries.one_unit_side import fourbody_geometry_sqrt83_sqrt3_sqrt3_sqrt3_sqrt3
from hydro4b_coords.geometries.one_unit_side import fourbody_geometry_sqrt83_sqrt3_sqrt3_sqrt3_sqrt113
from hydro4b_coords.geometries.one_unit_side import fourbody_geometry_sqrt3_sqrt3_sqrt3_sqrt113_2
from hydro4b_coords.geometries.one_unit_side import fourbody_geometry_sqrt3_sqrt3_2_2_2
from hydro4b_coords.geometries.one_unit_side import fourbody_geometry_sqrt3_sqrt113_sqrt113_sqrt113_sqrt113
from hydro4b_coords.geometries.one_unit_side import fourbody_geometry_sqrt3_sqrt113_sqrt113_sqrt113_2

from hydro4b_coords.geometries.combinatorics import MAP_GEOMETRY_TAG_TO_COMBINATORIAL_COUNT

MAP_GEOMETRY_TAG_TO_FUNCTION = {
    '1'                                     : tetrahedron,
    'sqrt2'                                 : fourbody_geometry_sqrt2,
    'sqrt83'                                : fourbody_geometry_sqrt83,
    'sqrt3'                                 : fourbody_geometry_sqrt3,
    'sqrt2_sqrt2'                           : fourbody_geometry_sqrt2_sqrt2,
    'sqrt2_sqrt113'                         : fourbody_geometry_sqrt2_sqrt113,
    'sqrt2_sqrt3'                           : fourbody_geometry_sqrt2_sqrt3,
    'sqrt83_sqrt113'                        : fourbody_geometry_sqrt83_sqrt113,
    'sqrt3_sqrt3'                           : fourbody_geometry_sqrt3_sqrt3,
    'sqrt3_sqrt113'                         : fourbody_geometry_sqrt3_sqrt113,
    'sqrt3_2'                               : fourbody_geometry_sqrt3_2,
    'sqrt113_sqrt113'                       : fourbody_geometry_sqrt113_sqrt113,
    'sqrt2_sqrt2_sqrt83'                    : fourbody_geometry_sqrt2_sqrt2_sqrt83,
    'sqrt2_sqrt2_sqrt113'                   : fourbody_geometry_sqrt2_sqrt2_sqrt113,
    'sqrt2_sqrt2_2'                         : fourbody_geometry_sqrt2_sqrt2_2,
    'sqrt2_sqrt83_sqrt113'                  : fourbody_geometry_sqrt2_sqrt83_sqrt113,
    'sqrt2_sqrt3_sqrt3_a'                   : fourbody_geometry_sqrt2_sqrt3_sqrt3_a,
    'sqrt2_sqrt3_sqrt3_b'                   : fourbody_geometry_sqrt2_sqrt3_sqrt3_b,
    'sqrt2_sqrt3_sqrt113_a'                 : fourbody_geometry_sqrt2_sqrt3_sqrt113_a,
    'sqrt2_sqrt3_sqrt113_b'                 : fourbody_geometry_sqrt2_sqrt3_sqrt113_b,
    'sqrt2_sqrt113_sqrt113_a'               : fourbody_geometry_sqrt2_sqrt113_sqrt113_a,
    'sqrt2_sqrt113_sqrt113_b'               : fourbody_geometry_sqrt2_sqrt113_sqrt113_b,
    'sqrt83_sqrt3_sqrt3'                    : fourbody_geometry_sqrt83_sqrt3_sqrt3,
    'sqrt83_sqrt3_sqrt113'                  : fourbody_geometry_sqrt83_sqrt3_sqrt113,
    'sqrt83_sqrt113_sqrt113'                : fourbody_geometry_sqrt83_sqrt113_sqrt113,
    'sqrt3_sqrt3_sqrt3_a'                   : fourbody_geometry_sqrt3_sqrt3_sqrt3_a,
    'sqrt3_sqrt3_sqrt3_b'                   : fourbody_geometry_sqrt3_sqrt3_sqrt3_b,
    'sqrt3_sqrt3_2_a'                       : fourbody_geometry_sqrt3_sqrt3_2_a,
    'sqrt3_sqrt3_2_b'                       : fourbody_geometry_sqrt3_sqrt3_2_b,
    'sqrt2_sqrt2_sqrt83_sqrt3'              : fourbody_geometry_sqrt2_sqrt2_sqrt83_sqrt3,
    'sqrt2_sqrt2_sqrt83_sqrt113'            : fourbody_geometry_sqrt2_sqrt2_sqrt83_sqrt113,
    'sqrt2_sqrt2_sqrt3_sqrt3_a'             : fourbody_geometry_sqrt2_sqrt2_sqrt3_sqrt3_a,
    'sqrt2_sqrt2_sqrt3_sqrt3_b'             : fourbody_geometry_sqrt2_sqrt2_sqrt3_sqrt3_b,
    'sqrt2_sqrt2_sqrt3_2'                   : fourbody_geometry_sqrt2_sqrt2_sqrt3_2,
    'sqrt2_sqrt3_sqrt3_sqrt3'               : fourbody_geometry_sqrt2_sqrt3_sqrt3_sqrt3,
    'sqrt2_sqrt3_sqrt3_sqrt113_a'           : fourbody_geometry_sqrt2_sqrt3_sqrt3_sqrt113_a,
    'sqrt2_sqrt3_sqrt3_sqrt113_b'           : fourbody_geometry_sqrt2_sqrt3_sqrt3_sqrt113_b,
    'sqrt2_sqrt3_sqrt3_sqrt113_c'           : fourbody_geometry_sqrt2_sqrt3_sqrt3_sqrt113_c,
    'sqrt2_sqrt3_sqrt3_2_a'                 : fourbody_geometry_sqrt2_sqrt3_sqrt3_2_a,
    'sqrt2_sqrt3_sqrt3_2_b'                 : fourbody_geometry_sqrt2_sqrt3_sqrt3_2_b,
    'sqrt2_sqrt3_sqrt3_2_c'                 : fourbody_geometry_sqrt2_sqrt3_sqrt3_2_c,
    'sqrt2_sqrt3_sqrt113_sqrt113_a'         : fourbody_geometry_sqrt2_sqrt3_sqrt113_sqrt113_a,
    'sqrt2_sqrt3_sqrt113_sqrt113_b'         : fourbody_geometry_sqrt2_sqrt3_sqrt113_sqrt113_b,
    'sqrt2_sqrt3_sqrt113_sqrt113_c'         : fourbody_geometry_sqrt2_sqrt3_sqrt113_sqrt113_c,
    'sqrt2_sqrt3_sqrt113_sqrt113_d'         : fourbody_geometry_sqrt2_sqrt3_sqrt113_sqrt113_d,
    'sqrt83_sqrt83_sqrt113_sqrt113'         : fourbody_geometry_sqrt83_sqrt83_sqrt113_sqrt113,
    'sqrt83_sqrt3_sqrt3_sqrt3'              : fourbody_geometry_sqrt83_sqrt3_sqrt3_sqrt3,
    'sqrt83_sqrt3_sqrt3_sqrt113'            : fourbody_geometry_sqrt83_sqrt3_sqrt3_sqrt113,
    'sqrt83_sqrt3_sqrt3_2'                  : fourbody_geometry_sqrt83_sqrt3_sqrt3_2,
    'sqrt83_sqrt3_sqrt113_sqrt113'          : fourbody_geometry_sqrt83_sqrt3_sqrt113_sqrt113,
    'sqrt83_sqrt113_sqrt113_sqrt113'        : fourbody_geometry_sqrt83_sqrt113_sqrt113_sqrt113,
    'sqrt83_sqrt113_sqrt113_2'              : fourbody_geometry_sqrt83_sqrt113_sqrt113_2,
    'sqrt3_sqrt3_sqrt3_sqrt113'             : fourbody_geometry_sqrt3_sqrt3_sqrt3_sqrt113,
    'sqrt3_sqrt3_sqrt3_2_a'                 : fourbody_geometry_sqrt3_sqrt3_sqrt3_2_a,
    'sqrt3_sqrt3_sqrt3_2_b'                 : fourbody_geometry_sqrt3_sqrt3_sqrt3_2_b,
    'sqrt3_sqrt3_sqrt3_2_c'                 : fourbody_geometry_sqrt3_sqrt3_sqrt3_2_c,
    'sqrt3_sqrt3_sqrt113_sqrt113_a'         : fourbody_geometry_sqrt3_sqrt3_sqrt113_sqrt113_a,
    'sqrt3_sqrt3_sqrt113_sqrt113_b'         : fourbody_geometry_sqrt3_sqrt3_sqrt113_sqrt113_b,
    'sqrt3_sqrt3_sqrt113_sqrt113_c'         : fourbody_geometry_sqrt3_sqrt3_sqrt113_sqrt113_c,
    'sqrt3_sqrt3_sqrt113_2'                 : fourbody_geometry_sqrt3_sqrt3_sqrt113_2,
    'sqrt3_sqrt3_2_2'                       : fourbody_geometry_sqrt3_sqrt3_2_2,
    'sqrt3_sqrt113_sqrt113_sqrt113'         : fourbody_geometry_sqrt3_sqrt113_sqrt113_sqrt113,
    'sqrt3_sqrt113_sqrt113_2'               : fourbody_geometry_sqrt3_sqrt113_sqrt113_2,
    'sqrt3_2_2_2'                           : fourbody_geometry_sqrt3_2_2_2,
    'sqrt2_sqrt2_sqrt83_sqrt3_sqrt3'        : fourbody_geometry_sqrt2_sqrt2_sqrt83_sqrt3_sqrt3,
    'sqrt2_sqrt2_sqrt83_sqrt3_sqrt113'      : fourbody_geometry_sqrt2_sqrt2_sqrt83_sqrt3_sqrt113,
    'sqrt2_sqrt2_sqrt3_sqrt3_sqrt113_a'     : fourbody_geometry_sqrt2_sqrt2_sqrt3_sqrt3_sqrt113_a,
    'sqrt2_sqrt2_sqrt3_sqrt3_sqrt113_b'     : fourbody_geometry_sqrt2_sqrt2_sqrt3_sqrt3_sqrt113_b,
    'sqrt2_sqrt2_sqrt3_sqrt3_2'             : fourbody_geometry_sqrt2_sqrt2_sqrt3_sqrt3_2,
    'sqrt2_sqrt2_sqrt3_sqrt113_2'           : fourbody_geometry_sqrt2_sqrt2_sqrt3_sqrt113_2,
    'sqrt2_sqrt2_sqrt113_sqrt113_2'         : fourbody_geometry_sqrt2_sqrt2_sqrt113_sqrt113_2,
    'sqrt2_sqrt83_sqrt3_sqrt3_sqrt113'      : fourbody_geometry_sqrt2_sqrt83_sqrt3_sqrt3_sqrt113,
    'sqrt2_sqrt3_sqrt3_sqrt3_sqrt3_a'       : fourbody_geometry_sqrt2_sqrt3_sqrt3_sqrt3_sqrt3_a,
    'sqrt2_sqrt3_sqrt3_sqrt3_sqrt3_b'       : fourbody_geometry_sqrt2_sqrt3_sqrt3_sqrt3_sqrt3_b,
    'sqrt2_sqrt3_sqrt3_sqrt3_sqrt113'       : fourbody_geometry_sqrt2_sqrt3_sqrt3_sqrt3_sqrt113,
    'sqrt2_sqrt3_sqrt3_sqrt113_sqrt113_a'   : fourbody_geometry_sqrt2_sqrt3_sqrt3_sqrt113_sqrt113_a,
    'sqrt2_sqrt3_sqrt3_sqrt113_sqrt113_b'   : fourbody_geometry_sqrt2_sqrt3_sqrt3_sqrt113_sqrt113_b,
    'sqrt83_sqrt3_sqrt3_sqrt3_sqrt3'        : fourbody_geometry_sqrt83_sqrt3_sqrt3_sqrt3_sqrt3,
    'sqrt83_sqrt3_sqrt3_sqrt3_sqrt113'      : fourbody_geometry_sqrt83_sqrt3_sqrt3_sqrt3_sqrt113,
    'sqrt3_sqrt3_sqrt3_sqrt113_2'           : fourbody_geometry_sqrt3_sqrt3_sqrt3_sqrt113_2,
    'sqrt3_sqrt3_2_2_2'                     : fourbody_geometry_sqrt3_sqrt3_2_2_2,
    'sqrt3_sqrt113_sqrt113_sqrt113_sqrt113' : fourbody_geometry_sqrt3_sqrt113_sqrt113_sqrt113_sqrt113,
    'sqrt3_sqrt113_sqrt113_sqrt113_2'       : fourbody_geometry_sqrt3_sqrt113_sqrt113_sqrt113_2,
}
# fmt: on
