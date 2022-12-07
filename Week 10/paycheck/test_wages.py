import pytest
import wages

def test_regular_hours():
    assert wages.get_regular_hours(20) == 20
    assert wages.get_regular_hours(40) == 40
    assert wages.get_regular_hours(50) == 40
    
def test_regular_pay():
    assert wages.get_regular_pay(20,15.5) == 310.0
    assert wages.get_regular_pay(40,25.95) == 1038.0
    assert wages.get_regular_pay(55,27.75) == 1110.0

def test_overtime_hours():
    assert wages.get_overtime_hours(20) == 0
    assert wages.get_overtime_hours(40) == 0
    assert wages.get_overtime_hours(50) == 10

def test_overtime_pay():
    assert wages.get_overtime_pay(20,20) == 0
    assert wages.get_overtime_pay(40,25.0) == 0
    assert wages.get_overtime_pay(50,50) == 750


if __name__ == "__main__":
    pytest.main()  