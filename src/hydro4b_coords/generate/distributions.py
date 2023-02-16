"""
This module contains factory functions that create specific DiscretizedDistributions.

TODO
- replace all assertions with proper exceptions
"""

import math

from hydro4b_coords.generate.discretized_distribution import DiscretizedDistribution


def exponential_decay_distribution(
    n_terms: int, x_min: float, x_max: float, *, coeff: float, decay_rate: float
) -> DiscretizedDistribution:
    assert coeff > 0.0
    assert decay_rate > 0.0
    assert x_max > x_min > 0.0

    def exponential_decay(x: float) -> float:
        return coeff * math.exp(-decay_rate * (x - x_min))

    return DiscretizedDistribution(exponential_decay, n_terms, x_min, x_max)
