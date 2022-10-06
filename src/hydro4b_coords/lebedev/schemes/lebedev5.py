"""
This module contains the angles and weights describing the Lebedev L = 5 scheme.
"""

import enum
import math

from hydro4b_coords.lebedev.orientation import LebedevOrientation
from hydro4b_coords.lebedev.schemes.schemeinfo import LebedevSchemeInfo


class Lebedev5(enum.Enum):
    ORIENT_X = enum.auto()
    ORIENT_Y = enum.auto()
    ORIENT_Z = enum.auto()
    ORIENT_A = enum.auto()
    ORIENT_B = enum.auto()
    ORIENT_C = enum.auto()
    ORIENT_D = enum.auto()


POLAR_ANGLE_A = 54.735610317245346 * (math.pi / 180.0)  # approx 0.955417 radians

LEBEDEV5_ANGLES = {
    Lebedev5.ORIENT_X: LebedevOrientation(0.5 * math.pi, 0.000000000000),
    Lebedev5.ORIENT_Y: LebedevOrientation(0.5 * math.pi, 0.50 * math.pi),
    Lebedev5.ORIENT_Z: LebedevOrientation(0.00000000000, 0.000000000000),
    Lebedev5.ORIENT_A: LebedevOrientation(POLAR_ANGLE_A, 0.25 * math.pi),
    Lebedev5.ORIENT_B: LebedevOrientation(POLAR_ANGLE_A, 0.75 * math.pi),
    Lebedev5.ORIENT_C: LebedevOrientation(POLAR_ANGLE_A, 1.25 * math.pi),
    Lebedev5.ORIENT_D: LebedevOrientation(POLAR_ANGLE_A, 1.75 * math.pi),
}


LEBEDEV5_WEIGHTS = [
    2.0 / 15.0,
    2.0 / 15.0,
    2.0 / 15.0,
    3.0 / 20.0,
    3.0 / 20.0,
    3.0 / 20.0,
    3.0 / 20.0,
]


LEBEDEV5_ORDERED_ORIENTATIONS = [
    Lebedev5.ORIENT_X,
    Lebedev5.ORIENT_Y,
    Lebedev5.ORIENT_Z,
    Lebedev5.ORIENT_A,
    Lebedev5.ORIENT_B,
    Lebedev5.ORIENT_C,
    Lebedev5.ORIENT_D,
]

LEBEDEV5_SCHEME_INFO = LebedevSchemeInfo(
    LEBEDEV5_ANGLES,
    LEBEDEV5_WEIGHTS,
    LEBEDEV5_ORDERED_ORIENTATIONS,
    len(LEBEDEV5_ORDERED_ORIENTATIONS),
)
