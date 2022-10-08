"""
LebedevOrientationGenerator
 - a generator that iterates over all combinations of Lebedev orientations
"""

from __future__ import annotations

import itertools

from hydro4b_coords.lebedev.orientation import LebedevOrientation
from hydro4b_coords.lebedev.schemes import LebedevScheme
from hydro4b_coords.lebedev.schemes import LEBEDEV_SCHEME_MAP


def total_number_of_orientations(scheme: LebedevScheme, n_particles: int) -> int:
    """Calculate the total number of different combinations of orientations."""
    if n_particles < 1:
        raise ValueError(
            "At least one particle is needed to calculate the total number of orientations.\n"
            f"Entered: {n_particles}"
        )
    
    scheme_info = LEBEDEV_SCHEME_MAP[scheme]  # type: ignore
    n_orients = scheme_info.n_orientations
    
    return n_orients ** n_particles


class LebedevOrientationGenerator:
    _orientations: list[LebedevScheme]
    _orientations_to_angles_map: dict[LebedevScheme, LebedevOrientation]
    _n_yielded_orients: int

    def __init__(self, scheme: LebedevScheme, n_yielded_orients: int) -> None:
        """
        scheme:
            the kind of lebedev orientation to be yielded by the iterator
        n_yielded_orients:
            the number of lebedev orientations to be yielded by each call to the iterator
        """
        scheme_info = LEBEDEV_SCHEME_MAP[scheme]  # type: ignore
        self._orientations = scheme_info.ordered_orientations
        self._orientations_to_angles_map = scheme_info.angles

        self.set_number_of_yielded_orientations(n_yielded_orients)

    def set_number_of_yielded_orientations(self, n_yielded_orients: int) -> None:
        if n_yielded_orients < 1:
            raise ValueError(
                "The LebedevOrientationGenerator must yield a positive number of orientations\n"
                "with each call.\n"
                f"Entered: {n_yielded_orients}"
            )
        self._n_yielded_orients = n_yielded_orients

    def combination(self, *indices: int) -> list[LebedevScheme]:
        return [self._orientations[i] for i in indices]

    @property
    def number_of_orientations(self) -> int:
        return len(self._orientations)

    @property
    def orientations_to_angles_map(self) -> dict[LebedevScheme, LebedevOrientation]:
        return self._orientations_to_angles_map

    def __iter__(self):
        n_total_orients = len(self._orientations)
        self._product_indices = itertools.product(
            range(n_total_orients), repeat=self._n_yielded_orients
        )

        return self

    def __next__(self):
        next_indices = next(self._product_indices)
        return self.combination(*next_indices)
