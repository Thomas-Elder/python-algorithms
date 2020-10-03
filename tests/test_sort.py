import pytest
from algorithms.sort import insertion 

@pytest.fixture
def test_list():

    return [5, 4, 3, 2, 1]

class Test_Insertion:

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    def test_sort(self, test_list):
        expected = [1, 2, 3, 4, 5]

        sorter = insertion.Insertion()
        result = sorter.sort(test_list)

        assert result == expected