"""This is the test file for module series.py."""
import pytest

# for testing fibonacci
# pairs: (n, expected_result)
fib_n_values = [
    (0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (13, 233),
    (20, 6765), (30, 832040)
]

lucas_n_values = [
    (0, 2), (1, 1), (2, 3), (3, 4), (4, 7), (5, 11), (6, 18), (13, 521),
    (20, 15127), (30, 1860498)
]


@pytest.mark.parametrize('n, result', fib_n_values)
def test_fib(n, result):
    """Test for fib using n_values list."""
    from series import fib
    assert fib(n) == result


@pytest.mark.parametrize('n, result', lucas_n_values)
def test_lucas(n, result):
    """Test for lucas series using n_values list."""
    from series import lucas
    assert lucas(n) == result


@pytest.mark.parametrize('n, result', fib_n_values)
def test_sum_series(n, result):
    """Test for sum_series default using n_values list."""
    from series import sum_series
    assert sum_series(n) == result


@pytest.mark.parametrize('n, result', lucas_n_values)
def test_sum_series_lucas(n, result):
    """Test for sum_series lucas using n_values list."""
    from series import sum_series
    assert sum_series(n, 2, 1) == result
