import math

import pytest

from cartesian import Cartesian3D
from cartesian import measure

from hydro4b_coords.spherical import Spherical3D
from hydro4b_coords.spherical import hydrogen_molecule_atomic_positions
from hydro4b_coords.spherical import spherical_to_cartesian
import hydro4b_coords.lebedev as lebedev


class TestSpherical3D:
    @pytest.mark.parametrize(
        "polar, azimuthal, expect_point",
        [
            (0.0 * math.pi, 0.0 * math.pi, Cartesian3D(0.0, 0.0, 1.0)),
            (0.5 * math.pi, 0.0 * math.pi, Cartesian3D(1.0, 0.0, 0.0)),
            (0.5 * math.pi, 0.5 * math.pi, Cartesian3D(0.0, 1.0, 0.0)),
            (0.5 * math.pi, 1.0 * math.pi, Cartesian3D(-1.0, 0.0, 0.0)),
            (0.5 * math.pi, 1.5 * math.pi, Cartesian3D(0.0, -1.0, 0.0)),
            (1.0 * math.pi, 0.0 * math.pi, Cartesian3D(0.0, 0.0, -1.0)),
        ],
    )
    def test_axis_orientations(self, polar, azimuthal, expect_point):
        sph_point = Spherical3D(1.0, polar, azimuthal)
        actual_point = spherical_to_cartesian(sph_point)

        assert measure.approx_eq(actual_point, expect_point)

    @pytest.mark.parametrize(
        "polar, azimuthal, expect_point",
        [
            (
                0.5 * math.pi,
                0.25 * math.pi,
                Cartesian3D(math.sqrt(0.5), math.sqrt(0.5), 0.0),
            ),
            (
                0.5 * math.pi,
                0.75 * math.pi,
                Cartesian3D(-math.sqrt(0.5), math.sqrt(0.5), 0.0),
            ),
            (
                0.5 * math.pi,
                1.25 * math.pi,
                Cartesian3D(-math.sqrt(0.5), -math.sqrt(0.5), 0.0),
            ),
            (
                0.5 * math.pi,
                1.75 * math.pi,
                Cartesian3D(math.sqrt(0.5), -math.sqrt(0.5), 0.0),
            ),
        ],
    )
    def test_45deg_along_xyplane(self, polar, azimuthal, expect_point):
        sph_point = Spherical3D(1.0, polar, azimuthal)
        actual_point = spherical_to_cartesian(sph_point)

        assert measure.approx_eq(actual_point, expect_point)

    @pytest.mark.parametrize(
        "polar, expect_point",
        [
            (0.0, Cartesian3D(0.0, 0.0, 1.0)),
            (math.pi, Cartesian3D(0.0, 0.0, -1.0)),
        ],
    )
    def test_azimuthal_invariance_at_poles(self, polar, expect_point):
        length = 1.0

        n_steps = 20
        azimuthal_step = 2.0 * math.pi / (n_steps - 1)

        for i in range(n_steps):
            azimuthal = i * azimuthal_step
            sph_point = Spherical3D(1.0, polar, azimuthal)
            actual_point = spherical_to_cartesian(sph_point)

            assert measure.approx_eq(actual_point, expect_point)

    @pytest.mark.parametrize("length", [0.0, -1.0])
    def test_exception_nonpositive_length(self, length):
        with pytest.raises(ValueError) as exc_info:
            Spherical3D(length, 0.0, 0.0)

        assert "Distance from origin to point must be positive." in str(exc_info.value)


class TestHydrogenMoleculeAtomicPositions:
    @pytest.mark.parametrize(
        "orientation, expect_point0, expect_point1",
        [
            (
                lebedev.Lebedev3.ORIENT_X,
                Cartesian3D(1.0, 0.0, 0.0),
                Cartesian3D(-1.0, 0.0, 0.0),
            ),
            (
                lebedev.Lebedev3.ORIENT_Y,
                Cartesian3D(0.0, 1.0, 0.0),
                Cartesian3D(0.0, -1.0, 0.0),
            ),
            (
                lebedev.Lebedev3.ORIENT_Z,
                Cartesian3D(0.0, 0.0, 1.0),
                Cartesian3D(0.0, 0.0, -1.0),
            ),
        ],
    )
    def test_lebedev3(self, orientation, expect_point0, expect_point1):
        centre = Cartesian3D.origin()
        bondlength = 2.0

        angles = lebedev.schemes.lebedev3.LEBEDEV3_ANGLES[orientation]

        point0, point1 = hydrogen_molecule_atomic_positions(
            centre, bondlength, angles.polar, angles.azimuthal
        )

        assert measure.approx_eq(point0, expect_point0)
        assert measure.approx_eq(point1, expect_point1)

    def test_both_points_same_distance_from_centre(self):
        centre = Cartesian3D(-0.5, 0.125, 0.75)
        bondlength = 2.0
        polar = 1.2345
        azimuthal = 2.3456

        point0, point1 = hydrogen_molecule_atomic_positions(
            centre, bondlength, polar, azimuthal
        )

        dist0 = measure.euclidean_distance(centre, point0)
        dist1 = measure.euclidean_distance(centre, point1)

        assert dist0 == pytest.approx(dist1)
