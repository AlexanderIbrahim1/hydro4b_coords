"""
Methods to confirm that certain requirements are satisfied, and if not, an
exception is raised.
"""


def _check_lat_const_positive(lat_const: float) -> None:
    if lat_const <= 0.0:
        raise ValueError(f"The lattice constant must be positive. Entered: {lat_const}")
