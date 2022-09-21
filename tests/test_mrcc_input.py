import pytest

from hydro4b_coords.mrcc_input import MRCCInputFileData


class TestMRCCInputFileData:
    @pytest.mark.parametrize('ccsdt', ['ccsd(t)', 'CCSD(T)', 'CcSd(T)'])
    def test_set_calc_cases(self, ccsdt):
        mrccdata = MRCCInputFileData()
        mrccdata.set_calc(ccsdt)
        assert mrccdata.fields['calc'] == 'ccsd(t)'
        
    
    def test_set_calc(self):
        mrccdata = MRCCInputFileData()
        mrccdata.set_calc('ccsd(t)')
        assert mrccdata.fields['calc'] == 'ccsd(t)'
    
    def test_set_calc_raisees(self):
        mrccdata = MRCCInputFileData()
        with pytest.raises(ValueError):
            mrccdata.set_calc('whatever')
