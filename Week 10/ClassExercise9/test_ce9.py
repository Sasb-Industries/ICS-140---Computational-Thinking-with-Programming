""" 
Use this file to complete the programming exercise in class exercise 9. 
Do not make changes to this file.

This file is used to run automated tests for the class exercise
If you have not already installed pytest run the following command:

pip install pytest

"""

import pytest
import class_exercise_9 as ce9

def test_add():
    # contains 3 test cases for the add function
    assert ce9.add(1,2) == 3
    assert ce9.add(3,4) == 7
    assert ce9.add(5,3) == 8

def test_subtract():
    # contains 3 test cases for the subtract function
    assert ce9.subtract(1,0) == 1
    assert ce9.subtract(3,4) == -1
    assert ce9.subtract(5,3) == 2

def test_multiply():
    # contains 3 test cases for the multiply function
    assert ce9.multiply(1,2) == 2
    assert ce9.multiply(3,4) == 12
    assert ce9.multiply(5,3) == 15

def test_divide():
    # contains 3 test cases for the divide function
    quotient, remainder = ce9.divide(1,2)
    assert quotient == 0
    assert remainder == 1
    quotient, remainder = ce9.divide(12,4)
    assert quotient == 3
    assert remainder == 0
    quotient, remainder = ce9.divide(18,4)
    assert quotient == 4
    assert remainder == 2

if __name__ == '__main__':
    pytest.main()