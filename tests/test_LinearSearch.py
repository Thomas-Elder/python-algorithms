import pytest
from algorithms.search import linear 

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

        searcher = linear.LinearSearch()
        result = searcher.find(test_list, 5)

        assert result == expected