"""
LebedevOrientationGenerator
 - a generator that iterates over all combinations of Lebedev orientations
"""

from __future__ import annotations

import itertools
from typing import Optional

from hydro4b_coords.lebedev.schemes import LebedevScheme
from hydro4b_coords.lebedev.schemes import LEBEDEV_SCHEME_MAP


class LebedevOrientationGenerator:
    _orientations: list[LebedevScheme]
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

    def __iter__(self):
        n_total_orients = len(self._orientations)
        self._product_indices = itertools.product(
            range(n_total_orients), repeat=self._n_yielded_orients
        )

        return self

    def __next__(self):
        next_indices = next(self._product_indices)
        return self.combination(*next_indices)
