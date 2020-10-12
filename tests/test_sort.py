import pytest
from algorithms.sort.insertion import insertion
from algorithms.sort.merge import merge
from algorithms.sort.bubble import bubble
from algorithms.sort.bubble import bubble_recursive
from algorithms.sort.heap import heap
from algorithms.sort.quick import quick
from algorithms.sort.selection import selection

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

        result = insertion(test_list)

        assert result == expected

    def test_sortDescending(self, test_list):
        expected = [5, 4, 3, 2, 1]

        result = insertion(test_list, order='descending')

        assert result == expected

class Test_Selection:

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    def test_sortAscending(self, test_list):
        expected = [1, 2, 3, 4, 5]

        result = selection(test_list)

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

    def test_sortDescending(self, test_list):
        expected = [5, 4, 3, 2, 1]

        result = bubble(test_list, order='descending')

        assert result == expected

class Test_BubbleRecursive:

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    def test_sortAscending(self, test_list):
        expected = [1, 2, 3, 4, 5]

        result = bubble_recursive(test_list)

        assert result == expected

class Test_Heap:

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    def test_sortAscending(self, test_list):
        expected = [1, 2, 3, 4, 5]

        result = heap(test_list)

        assert result == expected

class Test_Quick:

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    def test_sortAscending(self, test_list):
        expected = [1, 2, 3, 4, 5]

        result = quick(test_list, 0, len(test_list) - 1)

        assert result == expected