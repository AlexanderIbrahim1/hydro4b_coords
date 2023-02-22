"""
A four-body geometry of points cannot be uniquely described by its six side lengths,
unless the order of those side lengths is taken into account.

Two different four-body geometries might have the same set of six side lengths,
but in a different order.
"""

from typing import Tuple

from hydro4b_coords.sidelength_swap.common_types import SixSideLengths
from hydro4b_coords.sidelength_swap.swappers import SWAP_INDICES_FUNCTIONS


def repeated_index_swap_sort(
    sidelens: SixSideLengths,
    n_max_swap_sweeps: int = 1024,
) -> SixSideLengths:
    """
    Performs the index swaps over and over again until they no longer change the
    order of the six side lengths.
    """
    for _ in range(n_max_swap_sweeps):
        sidelens, n_swaps = index_swap_sort(sidelens)
        if n_swaps == 0:
            break

    return sidelens


def index_swap_sort(sidelens: SixSideLengths) -> Tuple[SixSideLengths, int]:
    """
    Attempt to perform all six index swaps on the tuple of sidelengths. Return both
    the final swapped indices, and the number of swaps performed.
    """
    n_swaps = 0
    for swap_func in SWAP_INDICES_FUNCTIONS:
        swapped_sidelens = swap_func(sidelens)
        if swapped_sidelens < sidelens:
            sidelens = swapped_sidelens
            n_swaps += 1

    return sidelens, n_swaps
