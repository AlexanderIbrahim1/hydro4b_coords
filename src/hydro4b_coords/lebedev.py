"""
This module contains the dictionaries that map the Lebedev angular orientations
to (polar, azimuthal) angle pairs.
"""

from __future__ import annotations

import copy
import dataclasses
import enum
import itertools
import math

from typing import Sequence
from typing import TypeVar


@dataclasses.dataclass(frozen=True)
class LebedevOrientation:
    polar: float
    azimuthal: float


class Lebedev3(enum.Enum):
    ORIENT_X = enum.auto()
    ORIENT_Y = enum.auto()
    ORIENT_Z = enum.auto()


LEBEDEV3_ANGLES = {
    Lebedev3.ORIENT_X: LebedevOrientation(0.5 * math.pi, 0.0),
    Lebedev3.ORIENT_Y: LebedevOrientation(0.5 * math.pi, 0.5 * math.pi),
    Lebedev3.ORIENT_Z: LebedevOrientation(0.0, 0.0),
}

# NOTE: several operations depend on the order of the orientations with a given
# Lebedev scheme to be the same each time. Even though both enums and dictionaries
# in Python are ordered, I would prefer to have an object that *explicitly* orders them
LEBEDEV3_ORDERED_ORIENTATIONS = [
    Lebedev3.ORIENT_X,
    Lebedev3.ORIENT_Y,
    Lebedev3.ORIENT_Z,
]


class Lebedev5(enum.Enum):
    ORIENT_X = enum.auto()
    ORIENT_Y = enum.auto()
    ORIENT_Z = enum.auto()
    ORIENT_A = enum.auto()
    ORIENT_B = enum.auto()
    ORIENT_C = enum.auto()
    ORIENT_D = enum.auto()


Orientations = TypeVar("Orientations", Lebedev3, Lebedev5)


class LebedevOrientationGenerator:
    _orientations: list[Orientations]

    def __init__(self, lebedev_enum: Orientations) -> None:
        # if more lebedev schemes pop up, consider replacing this with a dict lookup
        if lebedev_enum == Lebedev3:
            self._orientations = copy.copy(LEBEDEV3_ORDERED_ORIENTATIONS)
        else:
            raise ValueError("Only the Lebedev-3 scheme has been implemented so far.")

    def combination(self, *indices: Sequence[int]) -> list[Orientations]:
        return [self._orientations[i] for i in indices]

    def set_n_yielded_orientations(self, n_yielded_orients: int) -> None:
        """Set the number of orientations to be yielded by each call to the iterator."""
        assert n_yielded_orients >= 1
        self.n_yielded_orients = n_yielded_orients

    def __iter__(self):
        n_total_orients = len(self._orientations)
        self._product_indices = itertools.product(
            *[range(n_total_orients) for _ in range(self.n_yielded_orients)]
        )

        return self

    def __next__(self):
        next_indices = next(self._product_indices)
        return self.combination(*next_indices)
