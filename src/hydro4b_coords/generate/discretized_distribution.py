"""
This module contains components for sampling points from 1D distributions.
"""

from __future__ import annotations
from typing import Any
from typing import Callable
from typing import Optional

import numpy as np


class DiscretizedDistribution:

    _linspace_domain: np.ndarray[float]
    _discretized_cdf: np.ndarray[float]

    def __init__(
        self,
        function: Callable[[Any], float],
        n_terms: int,
        x_min: float,
        x_max: float,
        *,
        args: Optional[list[Any]] = None,
        kwargs: Optional[dict[Any, Any]] = None,
    ) -> None:
        _check_number_of_terms(n_terms)
        _check_bounds_order(x_min, x_max)

        self._linspace_domain = np.linspace(x_min, x_max, n_terms)

        partial_func = _create_partial_func(function, args, kwargs)
        discretized = _discretize_pdf(partial_func, self._linspace_domain)
        normalized = discretized / np.sum(discretized)

        self._discretized_cdf = _zerobased_cumsum(normalized)

    def sample(self) -> float:
        """Sample a value from the discretized distribution."""
        prob = np.random.uniform(0.0, 1.0)
        x_sampled = np.interp(prob, self._discretized_cdf, self._linspace_domain)

        return x_sampled


def _zerobased_cumsum(normalized_pdf: np.ndarray[float]) -> np.ndarray[float]:
    """
    In the '_discretize_pdf' function, the returned array is 1 element shorter than
    then length of 'linspace_domain'.

    This allows us to tack on a value of 0.0 at the beginning of the array. There is
    an issue where, if the 0th element is not 0.0, then the first bin ends up being
    oversampled.
    """
    return np.concatenate(([0.0], np.cumsum(normalized_pdf)))


def _create_partial_func(
    function: Callable[[Any], float],
    args: Optional[list[Any]] = None,
    kwargs: Optional[dict[Any, Any]] = None,
) -> Callable[[float], float]:
    """
    Create a partial function of 'function', that accepts only one float, and returns only
    one float. Also checks 'args' and 'kwargs' before passing them.
    """
    if args is None:
        args = []

    if kwargs is None:
        kwargs = {}

    def partial_func(x: float) -> float:
        return function(x, *args, **kwargs)

    return partial_func


def _discretize_pdf(
    prob_dist_func: Callable[[float], float],
    linspace_domain: np.ndarray[float],
) -> np.ndarray[float]:
    """
    Evaluate a probability distribution function along a 1D domain. Because 'prob_dist_func'
    is assumed to represent a probability distribution function, all calls to it are checked
    to make sure they are nonnegative.

    To prevent an issue where the 0th element of the cumulative distribution is non-zero,
    the discretized PDF does not calculate the last element. The returned array is 1 element
    shorter than 'linspace_domain'.

    I couldn't think of an ideal, sound solution. However, the number of terms is typically
    large enough that the second-to-last value is pretty close to the last value anyways.

    Parameters
    ----------
    prob_dist_func
        - the probability distribution function to be discretized
    linspace_domain
        - a linearly-spaced array of values at which 'prob_dist_func' is evaluated

    Raises
    ------
    If 'prob_dist_func' returns a negative value when called, a ValueError is raised.
    """
    discretized = np.empty(linspace_domain.size - 1, dtype=float)
    for (i, x) in enumerate(linspace_domain[:-1]):
        value = prob_dist_func(x)
        _check_nonnegative(value, x)
        discretized[i] = value

    return discretized


def _check_nonnegative(value: float, x: float) -> None:
    if value < 0.0:
        raise ValueError(
            "All calls to the probability distribution function must evaluate to a nonnegative value.\n"
            f"Found: function evaluates to {value: .12f} at {x: .12f}"
        )


def _check_number_of_terms(n_terms: int) -> None:
    if n_terms < 3:
        raise ValueError(
            "To properly create the discretized probability distribution, the number of\n"
            "elements in the resulting array must be 3 or greater.\n"
            f"Entered: {n_terms}"
        )


def _check_bounds_order(x_min: float, x_max: float) -> None:
    if x_min >= x_max:
        raise ValueError(
            "'x_min' must be greater than 'x_max'.\n"
            f"Found: x_min = {x_min: .12f}, x_max = {x_max: .12f}"
        )
