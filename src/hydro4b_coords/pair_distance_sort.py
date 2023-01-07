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


def swap12(s: SixSideLengths) -> SixSideLengths:
    return (s[0], s[3], s[4], s[1], s[2], s[5])


def swap13(s: SixSideLengths) -> SixSideLengths:
    return (s[3], s[1], s[5], s[0], s[4], s[2])


def swap14(s: SixSideLengths) -> SixSideLengths:
    return (s[4], s[5], s[2], s[3], s[0], s[1])


def swap23(s: SixSideLengths) -> SixSideLengths:
    return (s[1], s[0], s[2], s[3], s[5], s[4])


def swap24(s: SixSideLengths) -> SixSideLengths:
    return (s[2], s[1], s[0], s[5], s[4], s[3])


def swap34(s: SixSideLengths) -> SixSideLengths:
    return (s[0], s[2], s[1], s[4], s[3], s[5])


def index_swap_sort(sidelens: SixSideLengths) -> SixSideLengths:
    swap_functions = [swap12, swap13, swap14, swap23, swap24, swap34]

    while True:
        n_swaps = 0
        for swap_func in swap_functions:
            swapped_sidelens = swap_func(sidelens)
            if swapped_sidelens < sidelens:
                sidelens = swapped_sidelens
                n_swaps += 1
        
        if n_swaps == 0:
            break

    return sidelens
