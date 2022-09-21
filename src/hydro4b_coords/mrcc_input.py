"""
This module contains functions for creating MRCC input files.
"""

from __future__ import annotations

from typing import Any
from typing import Optional

# set the calculation type
# set the memory

# set the CC parameters
# set the SCF parameters

# set the basis

# set the molecules
    # choosing which are ghosts and which aren't should be done outside the API

# set which are ghosts, by default


# PLAN
# one object collects the data about the MRCC file
# another takes the aforementioned 'data object', and creates the file

_CALC_OPTIONS = ['ccsd(t)']

def _err_msg_valid_options(func_name: str, option: str, valid_options: list[str]) -> str:
    err_msg_block = [
        f"'{option}' is not a valid option for '{func_name}'",
        "The valid options are:",
    ] + valid_options
    
    return '\n'.join(err_msg_block)


class MRCCInputFileData:
    """
    Instances of this class collects, verifies, sanitizes, and stores the
    information needed to create an MRCC input file. This instance is then
    passed to the MRCCInputFileCreator.
    """
    _fields: dict[Optional[str], Any]
    
    def __init__(self) -> None:
        self._fields = {
            'calc': None,
        }
    
    def set_calc(self, raw_calc: str) -> None:
        calc = raw_calc.lower()
        if calc not in _CALC_OPTIONS:
            err_msg = _err_msg_valid_options('setcalc', calc, _CALC_OPTIONS)
            raise ValueError(err_msg)
        
        self._fields['calc'] = calc
    
    @property
    def fields(self) -> dict[Optional[str], Any]:
        return self._fields
        
        


class MRCCInputFileCreator:
    pass
