"""This series defines functions that implement mathetmatical series."""


def fib(n):
    """Return the nth number from the Fibonacci series."""
    if n < 0:
        raise ValueError('n cannot be negative')
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def lucas(n):
    """Return the nth number from the Lucas series."""
    if n < 0:
        raise ValueError('n cannot be negative')
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)


def sum_series(n, a=0, b=1):
    """
    Return the nth number from a series based on optional parameters.
    If no values are passed for a and b the default series will be
    fibonocci.
    """
    if n < 0:
        raise ValueError('n cannot be negative')
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        return sum_series(n - 1, a, b) + sum_series(n - 2, a, b)


if __name__ == '__main__':
    print(__doc__)
    print()
    print('fib(n):')
    print(fib.__doc__)
    print('>>> fib(5)')
    print('>>>', fib(5))
    print()
    print('lucas(n):')
    print(lucas.__doc__)
    print('>>> lucas(5)')
    print('>>>', lucas(5))
    print()
    print('sum_series(n):')
    print(sum_series.__doc__)
    print('>>> sum_series(5)')
    print('>>>', sum_series(5))
    print(__name__)
