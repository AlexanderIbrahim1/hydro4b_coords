"""
A four-body geometry of points cannot be uniquely described by its six side lengths,
unless the order of those side lengths is taken into account.

Two different four-body geometries might have the same set of six side lengths,
but in a different order.

TODO: improve this module's description.
"""

from typing import Callable
from typing import Tuple

SixSideLengths = Tuple[float, float, float, float, float, float]


def swap_indices_12(s: SixSideLengths) -> SixSideLengths:
    return (s[0], s[3], s[4], s[1], s[2], s[5])


def swap_indices_13(s: SixSideLengths) -> SixSideLengths:
    return (s[3], s[1], s[5], s[0], s[4], s[2])


def swap_indices_14(s: SixSideLengths) -> SixSideLengths:
    return (s[4], s[5], s[2], s[3], s[0], s[1])


def swap_indices_23(s: SixSideLengths) -> SixSideLengths:
    return (s[1], s[0], s[2], s[3], s[5], s[4])


def swap_indices_24(s: SixSideLengths) -> SixSideLengths:
    return (s[2], s[1], s[0], s[5], s[4], s[3])


def swap_indices_34(s: SixSideLengths) -> SixSideLengths:
    return (s[0], s[2], s[1], s[4], s[3], s[5])


SWAP_INDICES_FUNCTIONS = [
    swap_indices_12,
    swap_indices_13,
    swap_indices_14,
    swap_indices_23,
    swap_indices_24,
    swap_indices_34,
]


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


