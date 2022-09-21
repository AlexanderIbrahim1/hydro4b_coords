from __future__ import annotations

import copy
import enum
import itertools
from typing import Any
from typing import Sequence

from hydro4b_coords import geometries
from hydro4b_coords import lebedev
from hydro4b_coords import molecule

def main():
    centres_of_mass = geometries.tetrahedron(1.0)
    bondlength = 0.1

    lebedev_scheme = lebedev.Lebedev3
    lebedevgen = lebedev.LebedevOrientationGenerator(lebedev_scheme)
    lebedevgen.set_n_yielded_orientations(len(centres_of_mass))

    print(lebedevgen.combination(0, 0, 0, 1))

    for orientations in lebedevgen:
        for mol in molecule.get_molecules(centres_of_mass, orientations, bondlength):
            print(mol.atoms)
            print(mol.is_ghost)
        exit()


if __name__ == "__main__":
    main()
