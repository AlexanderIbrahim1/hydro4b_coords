"""
The LebedevOrientation class is a POD type that specifies a point on the surface
of the unit sphere.
"""

from __future__ import annotations

import dataclasses


@dataclasses.dataclass(frozen=True)
class LebedevOrientation:
    polar: float
    azimuthal: float
