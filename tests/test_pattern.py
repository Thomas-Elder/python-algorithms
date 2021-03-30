import pytest
from algorithms.pattern.fibonacci import fibonacci

@pytest.fixture
def test_fibonacci():

    return [1, 1, 2, 3, 5]

class Test_Pattern:

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

    def test_fibonacci(self, test_fibonacci):
        expected = test_fibonacci[4]

        result = fibonacci(5)

        assert result == expected