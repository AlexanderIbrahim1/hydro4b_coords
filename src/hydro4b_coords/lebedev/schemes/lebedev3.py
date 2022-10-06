"""
This module contains the angles and weights describing the Lebedev L = 3 scheme.
"""

import enum
import math

from hydro4b_coords.lebedev.orientation import LebedevOrientation
from hydro4b_coords.lebedev.schemes.schemeinfo import LebedevSchemeInfo


class Lebedev3(enum.Enum):
    ORIENT_X = enum.auto()
    ORIENT_Y = enum.auto()
    ORIENT_Z = enum.auto()


LEBEDEV3_ANGLES = {
    Lebedev3.ORIENT_X: LebedevOrientation(0.5 * math.pi, 0.0),
    Lebedev3.ORIENT_Y: LebedevOrientation(0.5 * math.pi, 0.5 * math.pi),
    Lebedev3.ORIENT_Z: LebedevOrientation(0.0, 0.0),
}


LEBEDEV3_WEIGHTS = [1.0 / 3.0, 1.0 / 3.0, 1.0 / 3.0]


LEBEDEV3_ORDERED_ORIENTATIONS = [
    Lebedev3.ORIENT_X,
    Lebedev3.ORIENT_Y,
    Lebedev3.ORIENT_Z,
]

LEBEDEV3_SCHEME_INFO = LebedevSchemeInfo(
    LEBEDEV3_ANGLES,
    LEBEDEV3_WEIGHTS,
    LEBEDEV3_ORDERED_ORIENTATIONS,
    len(LEBEDEV3_ORDERED_ORIENTATIONS),
)
