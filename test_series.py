"""This is the test file for module series.py."""
import pytest

# (n, result)
n_values = [
    (0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (13, 233),
    (20, 6765), (30, 832040)
]


@pytest.mark.parametrize('n, result', n_values)
def test_fib(n, result):
    """Test for fib using n_values list."""
    from series import fib
    assert fib(n) == result
