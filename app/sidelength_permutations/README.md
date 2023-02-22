# Sidelength Permutations

Right now, I'm having problems getting the index swapping code to work.
Maybe it's possible to have a situation where no single index swap leads to a smaller index?

To begin the investigation, I'm going to try to get all possible permtuations of (0, 1, 2, 3, 4, 5)
via tetrahedron index swaps.

The first thing I'll try is monte carlo.
- I've performed lots and lots of random swaps (~10000)
- each time I perform a swap, I check if I've gotten that permutation before, and if not, store it in a set
- the number of unique permutations maxes out at 24

How do I make use of this to get the smallest permutation?
- doing the random swaps would be far too slow
- do I just hardcode all 24 permutations, and check against each one?
  - [UPDATE] this is what I did, and it seems to have worked
