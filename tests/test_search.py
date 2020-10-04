import pytest
from algorithms.search.linear import linearSearch

@pytest.fixture
def test_list():

    return [4, 5, 2, 3, 1]

class Test_Insertion:

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    def test_find(self, test_list):
        expected = 1

        result = linearSearch(test_list, 5)

        assert result == expected

    def test_findFailure(self, test_list):
        expected = -1

        result = linearSearch(test_list, 6)

        assert result == expected