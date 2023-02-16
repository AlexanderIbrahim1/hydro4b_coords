"""
This module contains functions for generating groups of 4 points in Cartesian3D space
from a random distribution of relative pair distances.
"""

import math
from dataclasses import dataclass
from typing import Tuple

from cartesian import Cartesian3D

from hydro4b_coords.generate.discretized_distribution import DiscretizedDistribution

FourCartesianPoints = Tuple[Cartesian3D, Cartesian3D, Cartesian3D, Cartesian3D]

# create the distribution
# sample 6 side lengths
# try and create four points


def sample_fourbody_geometry(
    distrib: DiscretizedDistribution,
    *,
    return_n_reattempts: bool = False,
    n_max_reattempts: int = 1024,
) -> FourCartesianPoints | Tuple[FourCartesianPoints, int]:
    """
    Generate four Cartesian3D points, whose six relative side lengths are generated
    by the distribution 'distrib'.

    Because not every 6 randomly generated side lengths creates a valid four-body
    geometry, this function makes repeated attempts to generate the geometry, rejecting
    failed attempts.
    """

    n_reattempts = 0
    for _ in range(n_max_reattempts):
        try:
            pairdist_coord = _generate_pair_distances(distrib)
            points = _pairdistance_to_cartesian(pairdist_coord)
            break
        except ValueError:
            n_reattempts += 1
            continue

    _check_n_reattempts(n_reattempts, n_max_reattempts)

    if return_n_reattempts:
        return (points, n_reattempts)
    else:
        return points


@dataclass(frozen=True)
class PairDistanceCoordinate:
    r01: float
    r02: float
    r03: float
    r12: float
    r13: float
    r23: float

    def __post_init__(self) -> None:
        assert self._are_all_nonnegative()

    def unpack(self) -> Tuple[float, ...]:
        return (self.r01, self.r02, self.r03, self.r12, self.r13, self.r23)

    def _are_all_nonnegative(self) -> bool:
        """It does not make physical sense for a pair distance to be negative"""
        return all([pairdist >= 0.0 for pairdist in self.unpack()])


def _check_n_reattempts(n_reattempts: int, n_max_reattempts: int) -> None:
    if n_reattempts == n_max_reattempts:
        raise RuntimeError(
            "Unable to generate four Cartesian3D points with the provided distribution."
            f"Number of attempts: {n_reattempts}"
        )


def _generate_pair_distances(
    distrib: DiscretizedDistribution,
) -> PairDistanceCoordinate:
    n_pair_distances = 6
    pair_distances = [distrib.sample() for _ in range(n_pair_distances)]

    return PairDistanceCoordinate(*pair_distances)


def _pairdistance_to_cartesian(
    pairdists: PairDistanceCoordinate,
) -> FourCartesianPoints:
    """
    This function uses the 6 relative pair distances between the four points to
    recover four Cartesian points in 3D space.

    The four points returned satisfy the following properties:
     - point0 is at the origin
     - point1 lies on the positive x-axis
     - point2 satisfies (y >= 0, z == 0)
     - point3 satisfies (z >= 0)

    The 'pairdistance_to_cartesian()' and the 'cartesian_to_pairdistance()' functions
    are not inverses. We lose information when using the 'cartesian_to_pairdistance()'
    transformation. The relative pair distances only have 6 degrees of freedom (DOF) of
    information to work with, but the four Cartesian points have 12 DOF.

    The three DOF describing the centre of mass position of the four-body system are
    lost when converting from relative pair distances to Cartesian coordinates. The
    three DOF describing the orientation in space of the four-body system are also lost.
    """
    r01, r02, r03, r12, r13, r23 = pairdists.unpack()

    cos_theta102 = (r01**2 + r02**2 - r12**2) / (2.0 * r01 * r02)

    x2 = r02 * cos_theta102
    y2 = math.sqrt(r02**2 - x2**2)
    z2 = 0.0

    x3 = (r03**2 - r13**2 + r01**2) / (2.0 * r01)
    y3 = (r03**2 - r23**2 + r02**2 - 2.0 * x2 * x3) / (2.0 * y2)
    z3 = math.sqrt(r03**2 - x3**2 - y3**2)

    point0 = Cartesian3D(0.0, 0.0, 0.0)
    point1 = Cartesian3D(r01, 0.0, 0.0)
    point2 = Cartesian3D(x2, y2, z2)
    point3 = Cartesian3D(x3, y3, z3)

    return (point0, point1, point2, point3)
