"""
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given the below implementation of cons

implement car and cdr
"""
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(con):
    def _fun(a, b):
        return a
    return con(_fun)


def cdr(con):
    def _fun(a, b):
        return b
    return con(_fun)


if __name__ == "__main__":
    assert car(cons(3, 4)) == 3
    assert cdr(cons(3, 4)) == 4
