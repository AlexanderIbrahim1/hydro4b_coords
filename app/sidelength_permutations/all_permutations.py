"""
This module contains the code for trying to get all possible permutations of the
tuples (0, 1, 2, 3, 4, 5) via index swaps of a tetrahedron.
"""

import random
from typing import Tuple

from hydro4b_coords.sidelength_swap.swappers import SWAP_INDICES_FUNCTIONS

SixIntegers = Tuple[int, int, int, int, int, int]

class IntegerComparator:
    def less_than(self, s0: SixIntegers, s1: SixIntegers) -> bool:
        return s0 < s1

def monte_carlo_index_swapping(n_attempts: int):
    six_integers = (0, 1, 2, 3, 4, 5)
    permutations = set()
    permutations.add(six_integers)
    
    for _ in range(n_attempts):
        swap_func = random.sample(SWAP_INDICES_FUNCTIONS, 1)[0]
        six_integers = swap_func(six_integers)
        if six_integers not in permutations:
            permutations.add(six_integers)

    permutations = sorted(list(permutations))
    for p in permutations:
        print(p)

if __name__ == "__main__":
    n_attempts = 10000
    monte_carlo_index_swapping(n_attempts)

    
