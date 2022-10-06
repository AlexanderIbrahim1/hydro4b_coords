import dataclasses
from typing import Any

from hydro4b_coords.lebedev.orientation import LebedevOrientation

# NOTE: several operations depend on the order of the orientations with a given
# Lebedev scheme to be the same each time. Even though both `_angles` and
# `_ordered_orientations` have the same objects, and dictionaries are ordered in
# Python 3.6 and above, I would prefer to have an object that *explicitly* orders
# them; hence why `_ordered_orientations` exists
@dataclasses.dataclass(frozen=True)  # noqa
class LebedevSchemeInfo:
    angles: dict[Any, LebedevOrientation]
    weights: list[float]
    ordered_orientations: list[Any]
    n_orientations: int
