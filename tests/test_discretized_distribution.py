import pytest

from typing import Callable

from dataclasses import dataclass

import numpy as np

from hydro4b_coords.generate.discretized_distribution import _discretize_pdf
from hydro4b_coords.generate.discretized_distribution import DiscretizedDistribution


def test_discretize_pdf():
    """
    The '_discretize_pdf()' function should evaluate the entered function along
    the domain, and but skip the last value.
    """
    domain = np.linspace(0.0, 1.0, 6)

    mult_factor = 2.0
    linear = lambda x: mult_factor*x
    discretized = _discretize_pdf(linear, domain)

    for i in range(domain.size - 1):
        assert discretized[i] == pytest.approx(mult_factor*domain[i])


# --- TEST DISTRIBUTION PROPERTIES ---

@pytest.fixture(scope="class")
def linear01_samples():
    @dataclass
    class SamplesArguments:
        samples: list[float]
        x_min: float
        x_max: float

    function = lambda x: x
    n_terms = 6
    x_min = 0.0
    x_max = 1.0
    dd = DiscretizedDistribution(function, n_terms, x_min, x_max)

    n_samples = 1000
    samples = [dd.sample() for _ in range(n_samples)]

    yield SamplesArguments(samples, x_min, x_max)
    

@pytest.mark.usefixtures('linear01_samples')
class TestDiscretizedDistribution_probabilities:
    def test_samples_in_range(self, linear01_samples):
        l01 = linear01_samples
        is_in_range = lambda x : l01.x_min < x < l01.x_max
        assert all([is_in_range(s) for s in l01.samples])

    def test_more_samples_in_upper_half(self, linear01_samples):
        """
        The probability distribution is f(x) = x, on [x_min, x_max].
        There should be more samples above the midpoint than below.
        """
        l01 = linear01_samples
        x_mid = 0.5 * (l01.x_max + l01.x_min)
        n_greater_than_half = sum([s > x_mid for s in l01.samples])
        assert n_greater_than_half > len(l01.samples)/2


# --- TEST RAISING EXCEPTIONS ---
        
@pytest.fixture(scope="class")
def ddargs():
    @dataclass
    class DefaultDistributionArguments:
        function: Callable[[float], float]
        n_terms: int
        x_min: float
        x_max: float

    yield DefaultDistributionArguments(lambda x: x, 6, 0.0, 1.0)


@pytest.mark.usefixtures('ddargs')
class TestDiscretizedDistribution_raises:
    @pytest.mark.parametrize('n_terms', [-1, 0, 2])
    def test_raises_number_of_terms(self, ddargs, n_terms):
        with pytest.raises(ValueError):
            DiscretizedDistribution(
                ddargs.function,
                n_terms,
                ddargs.x_min,
                ddargs.x_max
            )
        
    @pytest.mark.parametrize('bad_x_pair', [(1.0, 1.0), (2.0, 1.5)])
    def test_raises_bounds_order(self, ddargs, bad_x_pair):
        x_min, x_max = bad_x_pair
        with pytest.raises(ValueError):
            DiscretizedDistribution(
                ddargs.function,
                ddargs.n_terms,
                x_min,
                x_max
            )

    def test_raises_nonnegative_values(self, ddargs):
        negative_valued_function = lambda x: -x
        with pytest.raises(ValueError):
            DiscretizedDistribution(
                negative_valued_function,
                ddargs.n_terms,
                ddargs.x_min,
                ddargs.x_max
            )

