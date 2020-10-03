
from algorithms.check import Check

def test_check():

    expected = 1
    result = Check().check()

    assert result == expected