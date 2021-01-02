def fib(n):
    """
    Write a recursive function to return the nth Fibonacci number.
    The Fibonacci sequence is
    0, 1, 1, 2, 3, 5, 8, 13, ....
    """
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def fib_iterative(n):
    """
    Write an iterative function to return the nth Fibonacci number.
    The Fibonacci sequence is
    0, 1, 1, 2, 3, 5, 8, 13, ....
    """
    a = 0
    b = 1
    if n == 1:
        return a
    if n == 2:
        return b
    i = 3
    while i <= n:
        tmp = b
        b = a + b
        a = tmp
        i += 1

    return b


if __name__ == "__main__":
    assert fib(1) == fib_iterative(1) == 0
    assert fib(2) == fib_iterative(2) == 1
    assert fib(7) == fib_iterative(7) == 8
    assert fib(8) == fib_iterative(8) == 13
