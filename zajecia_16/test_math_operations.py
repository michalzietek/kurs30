import pytest
from math_operations import add



@pytest.mark.parametrize("a, b, result",
                         [
                             (1, 1, 2),
                             (10, 10, 20),
                             (2, 2, 4)
                         ])
def test_add_2(a, b, result):
    assert add(a, b) == result