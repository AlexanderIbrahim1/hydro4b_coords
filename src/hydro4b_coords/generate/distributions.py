"""
This module contains factory functions that create specific DiscretizedDistributions.
"""

import math

from hydro4b_coords.generate.discretized_distribution import DiscretizedDistribution


def exponential_decay_distribution(
    n_terms: int, x_min: float, x_max: float, *, coeff: float, decay_rate: float
) -> DiscretizedDistribution:
    """Helper function for creating an exponential decay probability distribution."""
    _check_positive_coeff(coeff)
    _check_positive_decay_rate(decay_rate)

    def exponential_decay(x: float) -> float:
        return coeff * math.exp(-decay_rate * (x - x_min))

    return DiscretizedDistribution(exponential_decay, n_terms, x_min, x_max)


def _check_positive_coeff(coeff: float) -> None:
    if coeff <= 0.0:
        raise ValueError(
            "The coefficient of the exponential decay must be positive.\n"
            f"Found: coeff = {coeff: .12f}"
        )


def _check_positive_decay_rate(decay_rate: float) -> None:
    if decay_rate <= 0.0:
        raise ValueError(
            "The decay rate of the exponential decay must be positive.\n"
            f"Found: decay_rate = {decay_rate: .12f}"
        )
