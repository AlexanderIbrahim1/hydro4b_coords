"""
This module contains code for creating points in spherical coordinates, and
using them to create points in Cartesian3D space.
"""

from __future__ import annotations

import math

from cartesian import Cartesian3D


class Spherical3D:
    _length: float  # absolute distance from origin to point
    _polar: float  # polar angle *from* the positive z-axis, in radians
    _azimuthal: float  # azimuthal angle *from* the positive x-axis, in radians

    def __init__(self, length: float, polar: float, azimuthal: float) -> None:
        # NOTE:
        # the polar angle should always be between [0, pi];
        # however, the modulus operator makes it difficult to include the end-point
        # of a range, and writing `self._polar = polar % math.pi` will cause pi to
        # loop back around to 0.0
        #
        # the only solution I can think of (that doesn't depend on a small magic number by
        # which to extend the range) is to allow for the redundancy along [0, 2*pi)
        self._polar = polar % (2.0 * math.pi)

        self._length = length
        self._azimuthal = azimuthal % (2.0 * math.pi)

        if self._length <= 0.0:
            raise ValueError("Distance from origin to point must be positive.")

    @property
    def length(self) -> float:
        return self._length

    @property
    def polar(self) -> float:
        return self._polar

    @property
    def azimuthal(self) -> float:
        return self._azimuthal


def spherical_to_cartesian(sphpoint: Spherical3D) -> Cartesian3D:
    sin_pol = math.sin(sphpoint.polar)
    cos_pol = math.cos(sphpoint.polar)
    sin_azi = math.sin(sphpoint.azimuthal)
    cos_azi = math.cos(sphpoint.azimuthal)

    return Cartesian3D(
        sphpoint.length * cos_azi * sin_pol,
        sphpoint.length * sin_azi * sin_pol,
        sphpoint.length * cos_pol,
    )


def hydrogen_molecule_atomic_positions(
    centre_of_mass: Cartesian3D, bondlength: float, polar: float, azimuthal: float
) -> (Cartesian3D, Cartesian3D):
    """
    Create the positions of the two atoms in the hydrogen molecule, given the
    bond length of the molecule and its angular orientation relative to its
    centre of mass.
    """

    length = bondlength / 2.0

    sph_point1 = Spherical3D(length, polar, azimuthal)
    sph_point2 = Spherical3D(length, math.pi - polar, azimuthal + math.pi)

    car_point1 = spherical_to_cartesian(sph_point1)
    car_point2 = spherical_to_cartesian(sph_point2)

    return (centre_of_mass + car_point1, centre_of_mass + car_point2)
