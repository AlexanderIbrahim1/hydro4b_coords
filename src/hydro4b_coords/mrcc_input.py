"""
This module contains functions for creating MRCC input files.
"""

from __future__ import annotations

import sys

from typing import Any
from typing import Optional

from hydro4b_coords import molecule
from hydro4b_coords.molecule import HydrogenMoleculeInfo

from cartesian import operations


_CALC_OPTIONS = ["ccsd(t)"]
_ATOM_CENTRED_BASIS_OPTIONS = ["aug-cc-pVDZ", "aug-cc-pVTZ", "aug-cc-pVQZ"]
_MIDBOND_BASIS_OPTIONS = ["midbond-3s3p2d"]


def _funcname():
    """
    Returns the name of the function calling this function, by inspecting the
    stack frame. This is a somewhat hackish solution, so keep the magic code
    within here.
    """
    n_stacks_up = 1  # 0 -> return '_funcname', 1 -> return the calling function's name

    return sys._getframe(n_stacks_up).f_code.co_name


class MRCCInputFileData:
    """
    Instances of this class collects, verifies, sanitizes, and stores the
    information needed to create an MRCC input file. This instance is then
    passed to the MRCCInputFileCreator.
    """

    _fields: dict[Optional[str], Any]

    def __init__(self) -> None:
        self._fields = {
            "calc": None,
            "mem_mb": None,
            "cctol": None,
            "ccmaxit": None,
            "scftol": None,
            "scfdtol": None,
            "scfmaxit": None,
            "atom_basis": None,
            "midbond_basis": None,
            "molecules": None,
        }

    def _check_positive_int(self, func_name: str, value: int) -> str:
        if value <= 0:
            err_msg = "\n".join(
                [
                    f"'{func_name}' must accept a positive integer value",
                    f"Value entered: {value}",
                ]
            )
            raise ValueError(err_msg)

    def _check_valid_options(
        self, func_name: str, option: str, valid_options: list[str]
    ) -> str:
        if option not in valid_options:
            err_msg = "\n".join(
                [
                    f"'{option}' is not a valid option for '{func_name}'",
                    "The valid options are:",
                ]
                + valid_options
            )
            raise ValueError(err_msg)

    def set_calculation_type(self, calc: str) -> None:
        self._check_valid_options(_funcname(), calc.lower(), _CALC_OPTIONS)
        self._fields["calc"] = calc.lower()

    def set_memory_in_mb(self, mem_mb: int) -> None:
        self._check_positive_int(_funcname(), mem_mb)
        self._fields["mem_mb"] = f'{mem_mb}MB'

    def set_coupledcluster_tolerance(self, cctol: int) -> None:
        self._check_positive_int(_funcname(), cctol)
        self._fields["cctol"] = cctol

    def set_coupledcluster_maxiterations(self, ccmaxit: int) -> None:
        self._check_positive_int(_funcname(), ccmaxit)
        self._fields["ccmaxit"] = ccmaxit

    def set_scf_energy_tolerance(self, scftol: int) -> None:
        """
        Convergence threshold for the energy in SCF calculations. The energy will
        stop convenging when the change is less than 10^{-scftol} * Hartrees.
        """
        self._check_positive_int(_funcname(), scftol)
        self._fields["scftol"] = scftol

    def set_scf_density_tolerance(self, scfdtol: int) -> None:
        """
        Convergence threshold for the density matrix in SCF calculations. The RMS
        change in the density matrix will be smaller than 10^{-scfdtol}.
        """
        self._check_positive_int(_funcname(), scfdtol)
        self._fields["scfdtol"] = scfdtol

    def set_scf_maxiterations(self, scfmaxit: int) -> None:
        self._check_positive_int(_funcname(), scfmaxit)
        self._fields["scfmaxit"] = scfmaxit

    def set_atom_centred_basis(self, basis: str) -> None:
        self._check_valid_options(_funcname(), basis, _ATOM_CENTRED_BASIS_OPTIONS)
        self._fields["atom_basis"] = basis

    def set_midbond_basis(self, basis: str) -> None:
        self._check_valid_options(_funcname(), basis, _MIDBOND_BASIS_OPTIONS)
        self._fields["midbond_basis"] = basis

    def set_molecules(self, molecules: list[HydrogenMoleculeInfo]) -> None:
        # TODO: think of requirements for the list of hydrogen molecules; are there any?
        self._fields["molecules"] = molecules

    @property
    def fields(self) -> dict[Optional[str], Any]:
        return self._fields


class MRCCInputFileWriter:
    def __init__(self) -> None:
        pass
    
    def write_file(self, mrccdata: MRCCInputFileData, filename: str) -> str:
        calc_type_line = self._kvpair_line('calc', mrccdata.fields['calc'])
        memory_in_mb_line = self._kvpair_line('mem', mrccdata.fields['mem_mb'])
        cc_tolerance_line = self._kvpair_line('cctol', mrccdata.fields['cctol'])
        cc_maxiterations_line = self._kvpair_line('ccmaxit', mrccdata.fields['ccmaxit'])
        scf_energy_tolerance_line = self._kvpair_line('scftol', mrccdata.fields['scftol'])
        scf_density_tolerance_line = self._kvpair_line('scfdtol', mrccdata.fields['scfdtol'])
        scf_maxiterations_line = self._kvpair_line('scfmaxit', mrccdata.fields['scfmaxit'])
        
        basis_lines = self._basis_lines(mrccdata)
        geometry_lines = self._molecule_geometry_lines(mrccdata)
        
        with open(filename, 'w') as fout:
            contents = "\n".join(
                [
                    calc_type_line,
                    memory_in_mb_line,
                    cc_tolerance_line,
                    cc_maxiterations_line,
                    scf_energy_tolerance_line,
                    scf_density_tolerance_line,
                    scf_maxiterations_line,
                    "",
                    basis_lines,
                    "",
                    geometry_lines,
                ]
            )
            fout.write(contents)
    
    def _kvpair_line(self, key: str, value: Any, *, err_if_none: bool = True) -> str:
        if value is None:
            raise ValueError(f"The value for '{key}' cannot be None")
        return f"{key}={value}"

    def _basis_lines(self, mrccdata: MRCCInputFileData) -> str:
        """
        Write the set of lines that describe the atom-centred and (optionally) the
        midbond-centred basis sets used in the electronic structure calculation.
        """
        if mrccdata.fields["midbond_basis"] is not None:
            n_molecules = len(mrccdata.fields["molecules"])
            n_hydro_atoms_per_molecule = 2
            n_atoms = n_hydro_atoms_per_molecule * n_molecules
    
            basis_line = "\n".join(
                [
                    "basis=mixed",
                    "2",
                    f"{mrccdata.fields['atom_basis']} 1-{n_atoms}",
                    f"{mrccdata.fields['midbond_basis']} {n_atoms+1}",
                ]
            )
        else:
            basis_line = f"basis={mrccdata.fields['atom_basis']}"
    
        return basis_line

    def _molecule_geometry_lines(self, mrccdata: MRCCInputFileData) -> str:
        """
        Write the positions of all the hydrogen atoms, and optionally also the midbond
        ghost atom.
        """
        molecules = mrccdata.fields["molecules"]
        has_midbond = mrccdata.fields["midbond_basis"] is not None
    
        n_molecules = len(molecules)
        n_hydro_atoms_per_molecule = 2
        n_atoms = n_hydro_atoms_per_molecule * n_molecules
    
        position_header_lines = self._position_header_lines(n_atoms, has_midbond)
    
        atoms = molecule.atoms_from_molecules(molecules)
        ghost_statuses = molecule.ghost_status_from_molecules(molecules)
    
        # The midbond atom isn't a real atom, but rather just a position. However, in the
        # language of the MRCC program, the only way to include additional basis sets in space
        # is to create an atom and make it a ghost.
        # For the current project, it is located at the centroid of all the real atoms.
        if has_midbond:
            midbond_atom = operations.centroid(atoms)
            atoms.append(midbond_atom)
            ghost_statuses.append(True)
    
        atom_lines = "\n".join(
            [
                self._coordinates_line(atom, is_ghost=gstat)
                for (atom, gstat) in zip(atoms, ghost_statuses)
            ]
        )
        ghost_lines = self._ghost_indicator_lines(ghost_statuses)
    
        return "\n".join([position_header_lines, "", atom_lines, "", ghost_lines])

    def _position_header_lines(self, n_atoms: int, has_midbond: bool) -> str:
        if has_midbond:
            n_positions = n_atoms + 1
        else:
            n_positions = n_atoms
    
        position_header_lines = "\n".join(["unit=angs", "geom=xyz", f"{n_positions}"])
    
        return position_header_lines

    def _coordinates_line(self, atom: Cartesian3D, *, is_ghost: bool) -> str:
        """
        Format the line describing the atom and its cartesian position. Also included
        is a comment for the user, indicating whether or not that atom is a ghost.
        """
        atom_symbol = "H"
        x, y, z = atom.coordinates
    
        if is_ghost:
            comment = "# GHOST ATOM"
        else:
            comment = "# REAL ATOM"
    
        return f"{atom_symbol}   {x: 12.9f}   {y: 12.9f}   {z: 12.9f}   {comment}"

    def _ghost_indicator_lines(self, ghost_statuses: list[bool]) -> str:
        """
        A comma-separated list of indices indicating which of the atoms are ghost atoms.
        The MRCC code uses 1-index notation.
        """
        ghost_index_line = ",".join(
            [str(i + 1) for (i, status) in enumerate(ghost_statuses) if status]
        )
    
        ghost_lines = "\n".join(
            [
                "ghost=serialno",
                ghost_index_line,
            ]
        )
    
        return ghost_lines

