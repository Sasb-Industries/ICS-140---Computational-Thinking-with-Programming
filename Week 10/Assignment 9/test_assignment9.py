""" 
Use this file to complete assignment 9. Do not make changes to this file.

This file is used to run automated tests for the assignment
If you have not already installed pytest, run the following command:

pip install pytest

"""

import pytest
import assignment9 as a9

def test_county_tax():
    # contains 3 test cases for the county_tax function
    assert a9.county_tax(1000) == 25.0
    assert a9.county_tax(1234) == 30.85
    assert a9.county_tax(567.89) == 14.19725


def test_state_tax():
    # contains 3 test cases for the state_tax function
    assert a9.state_tax(1000) == 50.0
    assert a9.state_tax(1234) == 61.7
    assert a9.state_tax(567.89) == 28.3945


def test_total_tax():
    # contains 3 test cases for the total_tax function
    assert a9.total_tax(25.0, 50.0) == 75.0
    assert a9.total_tax(12.0, 34.0) == 46.0
    assert a9.total_tax(56.0, 78.0) == 134.0


if __name__ == '__main__':
    pytest.main()