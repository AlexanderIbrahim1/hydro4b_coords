from __future__ import annotations

import copy
import enum
import itertools
from typing import Any
from typing import Sequence

from hydro4b_coords import geometries
from hydro4b_coords import lebedev
from hydro4b_coords import molecule
from hydro4b_coords import mrcc_input

def get_molecules():
    centres_of_mass = geometries.tetrahedron(3.0)
    bondlength = 0.766777

    lebedev_scheme = lebedev.Lebedev3
    lebedevgen = lebedev.LebedevOrientationGenerator(lebedev_scheme)
    lebedevgen.set_n_yielded_orientations(len(centres_of_mass))

    orientations = lebedevgen.combination(1, 0, 2, 1)
    return molecule.get_molecules(centres_of_mass, orientations, bondlength)

def try_mrcc_input():
    mrccdata = mrcc_input.MRCCInputFileData()
    mrccdata.set_calculation_type('ccsd(t)')
    mrccdata.set_memory_in_mb(4096)
    mrccdata.set_coupledcluster_tolerance(9)
    mrccdata.set_coupledcluster_maxiterations(100)
    mrccdata.set_scf_energy_tolerance(7)
    mrccdata.set_scf_density_tolerance(7)
    mrccdata.set_scf_maxiterations(100)
    
    mrccdata.set_atom_centred_basis('aug-cc-pVDZ')
    mrccdata.set_midbond_basis('midbond-3s3p2d')
    
    molecules = get_molecules()
    molecules[0].set_ghost(True)
    mrccdata.set_molecules(molecules)
    
    filewriter = mrcc_input.MRCCInputFileWriter()
    
    filewriter.write_file(mrccdata, 'MINP')


if __name__ == "__main__":
    try_mrcc_input()
