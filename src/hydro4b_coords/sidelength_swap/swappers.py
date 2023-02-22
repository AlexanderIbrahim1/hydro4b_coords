"""
This module contains functions that permute the sidelengths in a tuple of six
sidelengths, in a way that corresponds to the  swapping of two indices in the
four-body geometry.
"""

from hydro4b_coords.sidelength_swap.common_types import SixSideLengths


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
