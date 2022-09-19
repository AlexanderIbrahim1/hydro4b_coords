"""
This module contains the dictionaries that map the Lebedev angular orientations
to (polar, azimuthal) angle pairs.
"""

import dataclasses
import enum
import math

@dataclasses.dataclass(frozen=True)
class LebedevOrientation:
    polar: float
    azimuthal: float

class Lebedev3(enum.Enum):
    ORIENT_X = enum.auto()
    ORIENT_Y = enum.auto()
    ORIENT_Z = enum.auto()

LEBEDEV3_ANGLES = {
    Lebedev3.ORIENT_X : LebedevOrientation(0.5*math.pi, 0.0),
    Lebedev3.ORIENT_Y : LebedevOrientation(0.5*math.pi, 0.5*math.pi),
    Lebedev3.ORIENT_Z : LebedevOrientation(0.0, 0.0),
}
