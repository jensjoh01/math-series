""""This is a module to create the Fibonacci and Lucas math series."""


def fib(n):
    """."""
    if n < 0:
        raise ValueError('n cannot be negative')
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def lucas(n):
    """."""
    if n < 0:
        raise ValueError('n cannot be negative')
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)
