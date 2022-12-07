""" 
Use this file to complete Lab 9. Do not make changes to this file.

This file is used to run automated tests for the lab
If you have not already installed pytest, run the following command:

pip install pytest

"""

import pytest
import lab9

def test_triangle_area():
    # contains 3 test cases for the triangle_area function
    assert lab9.triangle_area(1,2) == 1.0
    assert lab9.triangle_area(3,4) == 6.0
    assert lab9.triangle_area(5,3) == 7.5


def test_triangle_perimeter():
    # contains 3 test cases for the triangle_perimeter function
    assert lab9.triangle_perimeter(1,1,1) == 3
    assert lab9.triangle_perimeter(3,4,5) == 12
    assert lab9.triangle_perimeter(7,8,9) == 24



if __name__ == '__main__':
    pytest.main()