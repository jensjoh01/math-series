"""This is the test file for module series.py."""
import pytest


def test_fib_0():
    """Test for fib."""
    from series import fib
    assert fib(0) == 0


def test_fib_1():
    """Test for fib."""
    from series import fib
    assert fib(1) == 1


def test_fib_2():
    """Test for fib."""
    from series import fib
    assert fib(2) == 1


def test_fib_3():
    """Test for fib."""
    from series import fib
    assert fib(3) == 2


def test_fib_4():
    """Test for fib."""
    from series import fib
    assert fib(4) == 3


def test_fib_5():
    """Test for fib."""
    from series import fib
    assert fib(5) == 5
