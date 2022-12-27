# fmt: off
from hydro4b_coords.geometries.tetrahedra import tetrahedron
from hydro4b_coords.geometries.tetrahedra import irregular_tetrahedron
from hydro4b_coords.geometries.tetrahedra import irregular_tetrahedron_sqrt2
from hydro4b_coords.geometries.tetrahedra import irregular_tetrahedron_sqrt3
from hydro4b_coords.geometries.tetrahedra import irregular_tetrahedron_sqrt83

from hydro4b_coords.geometries.triangles import equilateral_triangle

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
# fmt: on
