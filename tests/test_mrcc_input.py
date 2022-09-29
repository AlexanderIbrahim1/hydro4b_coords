import pytest

from hydro4b_coords.mrcc_input import MRCCInputFileData
from hydro4b_coords.mrcc_input import MRCCInputFileWriter
from hydro4b_coords import geometries
from hydro4b_coords import lebedev
from hydro4b_coords import molecule
from hydro4b_coords import mrcc_input



class TestMRCCInputFileData:
    @pytest.mark.parametrize('ccsdt', ['ccsd(t)', 'CCSD(T)', 'CcSd(T)'])
    def test_set_calculation_type_cases(self, ccsdt):
        mrccdata = MRCCInputFileData()
        mrccdata.set_calculation_type(ccsdt)
        assert mrccdata.fields['calc'] == 'ccsd(t)'
        
    def test_set_calculation_type(self):
        mrccdata = MRCCInputFileData()
        mrccdata.set_calculation_type('ccsd(t)')
        assert mrccdata.fields['calc'] == 'ccsd(t)'
    
    def test_set_calculation_type_raises(self):
        mrccdata = MRCCInputFileData()
        with pytest.raises(ValueError) as exc_info:
            mrccdata.set_calculation_type('whatever')
        
        assert (
            "'whatever' is not a valid option for 'set_calculation_type'"
            in str(exc_info.value)
        )
    
    @pytest.mark.parametrize(
        'methodname, value, fieldname',
        [
            ('set_coupledcluster_tolerance', 9, 'cctol'),
            ('set_coupledcluster_maxiterations', 200, 'ccmaxit'),
            ('set_scf_energy_tolerance', 7, 'scftol'),
            ('set_scf_density_tolerance', 7, 'scfdtol'),
            ('set_scf_maxiterations', 100, 'scfmaxit'),
        ]
    )
    def test_positive_value_setters(self, methodname, value, fieldname):
        mrccdata = MRCCInputFileData()
        
        # a way to select the method to call by its string name
        method = getattr(mrccdata, methodname)
        method(value)
        
        assert mrccdata.fields[fieldname] == value
    
    def test_set_memory_in_mb(self):
        mrccdata = MRCCInputFileData()
        mrccdata.set_memory_in_mb(2048)
        mrccdata.fields['mem_mb'] == '2048MB'

    @pytest.mark.parametrize(
        'methodname, value',
        [
            ('set_memory_in_mb', -1024),
            ('set_memory_in_mb', 0),
            ('set_coupledcluster_tolerance', -9),
            ('set_coupledcluster_tolerance', 0),
            ('set_coupledcluster_maxiterations', -100),
            ('set_coupledcluster_maxiterations', 0),
            ('set_scf_energy_tolerance', -7),
            ('set_scf_energy_tolerance', 0),
            ('set_scf_density_tolerance', -7),
            ('set_scf_density_tolerance', 0),
            ('set_scf_maxiterations', -100),
            ('set_scf_maxiterations', 0),
        ]
    )
    def test_positive_value_setters_raises(self, methodname, value):
        mrccdata = MRCCInputFileData()
        with pytest.raises(ValueError) as exc_info:
            # a way to select the method to call by its string name
            method = getattr(mrccdata, methodname)
            method(value)
        
        assert (
            f"'{methodname}' must accept a positive integer value"
            in str(exc_info.value)
        )

def get_six_molecules() -> list[molecule.HydrogenMoleculeInfo]:
    """Some of the tests require molecules, and the only important aspect
    is the number of molecules present."""
    centres_of_mass = geometries.equilateral_triangle(1.0)
    bondlength = 0.1
    orientations = [
        lebedev.Lebedev3.ORIENT_X,
        lebedev.Lebedev3.ORIENT_Y,
        lebedev.Lebedev3.ORIENT_Z,
    ]
    
    molecules = molecule.get_molecules(centres_of_mass, orientations, bondlength)
    
    return molecules
    

def test_basis_lines_with_midbond():
    mrccdata = MRCCInputFileData()
    mrccdata.set_atom_centred_basis('aug-cc-pVDZ')
    mrccdata.set_midbond_basis('midbond-3s3p2d')
    
    molecules = get_six_molecules()
    mrccdata.set_molecules(molecules)
    
    expect_basis_lines = (
        "basis=mixed\n"
        "2\n"
        "aug-cc-pVDZ 1-6\n"
        "midbond-3s3p2d 7"
    )
    
    mrccwriter = MRCCInputFileWriter()
    
    assert mrccwriter._basis_lines(mrccdata) == expect_basis_lines

def test_basis_lines_without_midbond():
    mrccdata = MRCCInputFileData()
    mrccdata.set_atom_centred_basis('aug-cc-pVDZ')
    
    molecules = get_six_molecules()
    mrccdata.set_molecules(molecules)
    
    expect_basis_lines = 'basis=aug-cc-pVDZ'
    
    mrccwriter = MRCCInputFileWriter()
    assert mrccwriter._basis_lines(mrccdata) == expect_basis_lines

def test_ghost_indices_string():
    ghost_statuses = [True, False, True, True, False, False, True]
    expect_line = '\n'.join(['ghost=serialno', '1,3,4,7'])
    
    mrccwriter = MRCCInputFileWriter()
    assert mrccwriter._ghost_indicator_lines(ghost_statuses) == expect_line
