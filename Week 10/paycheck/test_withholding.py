import pytest
import withholding

def test_get_federal_taxes():
    assert withholding.get_federal_taxes(1000) == 136.0
    assert withholding.get_federal_taxes(2000) == 358.0
    assert withholding.get_federal_taxes(20000) == 6483.5


def test_get_state_mn_taxes():
    assert withholding.get_state_taxes_mn(1000) == 60.17
    assert withholding.get_state_taxes_mn(2000) == 130.9
    assert withholding.get_state_taxes_mn(20000) == 1869.1

    
if __name__ == "__main__":
    pytest.main()  