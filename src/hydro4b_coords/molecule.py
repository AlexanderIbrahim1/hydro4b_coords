"""
This module contains functions for creating the hydrogen molecules used in
the electronic structure input file.
"""

from __future__ import annotations
import enum

from cartesian import Cartesian3D

from hydro4b_coords import lebedev
from hydro4b_coords import spherical

class HydrogenMoleculeInfo:
    _atom0: Cartesian3D
    _atom1: Cartesian3D
    _is_ghost: bool

    def __init__(self, atom0: Cartesian3D, atom1: Cartesian3D) -> None:
        self._atom0 = atom0
        self._atom1 = atom1
        self._is_ghost = False

    def set_ghost(self, ghost: bool) -> None:
        """
        In the context of deciding which atoms are ghosts in an electronic structure
        calculation file, the atoms in a molecule must either both be ghost, or
        neither are ghost.
        """
        self.is_ghost = ghost

    @property
    def is_ghost(self) -> bool:
        return self._is_ghost

    @property
    def atoms(self) -> list[Cartesian3D]:
        return [self._atom0, self._atom1]

    @classmethod
    def from_orientation(
        cls, com: Cartesian3D, orientation: lebedev.Lebedev3, bondlength: float
    ) -> HydrogenMoleculeInfo:
        angles = lebedev.LEBEDEV3_ANGLES[orientation]
        atoms = spherical.hydrogen_molecule_atomic_positions(
            com, bondlength, angles.polar, angles.azimuthal
        )

        return HydrogenMoleculeInfo(atoms[0], atoms[1])


def get_molecules(
    centres_of_mass: list[Cartesian3D], orientations: list[enum.Enum], bondlength: float
) -> list[HydrogenMoleculeInfo]:
    return [
        HydrogenMoleculeInfo.from_orientation(com, orient, bondlength)
        for (com, orient) in zip(centres_of_mass, orientations)
    ]
