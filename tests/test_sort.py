import pytest
from algorithms.sort.insertion import insertion
from algorithms.sort.merge import merge
from algorithms.sort.bubble import bubble

@pytest.fixture
def test_list():

    return [4, 5, 2, 3, 1]

class Test_Insertion:

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    def test_sortAscending(self, test_list):
        expected = [1, 2, 3, 4, 5]

        result = insertion(test_list, order='ascending')

        assert result == expected

    def test_sortDescending(self, test_list):
        expected = [5, 4, 3, 2, 1]

        result = insertion(test_list, order='descending')

        assert result == expected

class Test_Merge:

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    def test_sortAscending(self, test_list):
        expected = [1, 2, 3, 4, 5]

        result = merge(test_list)

        assert result == expected

class Test_Bubble:

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    def test_sortAscending(self, test_list):
        expected = [1, 2, 3, 4, 5]

        result = bubble(test_list)

        assert result == expected