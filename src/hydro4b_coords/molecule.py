"""
This module contains functions for creating the hydrogen molecules used in
the electronic structure input file.
"""

from __future__ import annotations

from cartesian import Cartesian3D

from hydro4b_coords.lebedev import LebedevScheme
from hydro4b_coords.lebedev import LebedevOrientation
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
        self._is_ghost = ghost

    @property
    def is_ghost(self) -> bool:
        return self._is_ghost

    @property
    def atoms(self) -> list[Cartesian3D]:
        return [self._atom0, self._atom1]

    @classmethod
    def from_orientation(
        cls, com: Cartesian3D, sphere_angles: LebedevOrientation, bondlength: float
    ) -> HydrogenMoleculeInfo:
        atoms = spherical.hydrogen_molecule_atomic_positions(
            com, bondlength, sphere_angles.polar, sphere_angles.azimuthal
        )

        return HydrogenMoleculeInfo(atoms[0], atoms[1])  # type: ignore


def get_molecules(
    centres_of_mass: list[Cartesian3D],
    orientations: list[LebedevScheme],
    angle_map: dict[LebedevScheme, LebedevOrientation],
    bondlength: float,
) -> list[HydrogenMoleculeInfo]:
    assert len(centres_of_mass) == len(orientations)

    sphere_angles = [angle_map[orient] for orient in orientations]

    return [
        HydrogenMoleculeInfo.from_orientation(com, angles, bondlength)
        for (com, angles) in zip(centres_of_mass, sphere_angles)
    ]


def atoms_from_molecules(molecules: list[HydrogenMoleculeInfo]) -> list[Cartesian3D]:
    """Convenience function to extract the atom positions from the molecules."""
    atom_positions = list()
    for mol in molecules:
        atom_positions.extend(mol.atoms)

    return atom_positions


def ghost_status_from_molecules(molecules: list[HydrogenMoleculeInfo]) -> list[bool]:
    """Convenience function to extract the 'is_ghost' attribute of each atom from the molecules."""
    ghost_statuses = list()
    for mol in molecules:
        mol_ghosts = [mol.is_ghost] * 2
        ghost_statuses.extend(mol_ghosts)

    return ghost_statuses
