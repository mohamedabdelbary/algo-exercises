from collections import namedtuple

from nose.tools import assert_equals


class Cons(namedtuple('Cons', ['head', 'tail'])):

    @classmethod
    def from_array(cls, arr):
        raise NotImplementedError

    def to_array(self):
        raise NotImplementedError

    def filter(self, fn):
        raise NotImplementedError

    def map(self, fn):
        raise NotImplementedError

    def zip(self, other):
        raise NotImplementedError


assert_equals(Cons.from_array([]), None)
assert_equals(Cons.from_array([1]), Cons(1, None))
assert_equals(Cons.from_array([1, 2]), Cons(1, Cons(2, None)))

assert_equals(Cons.from_array([1, 2, 3, 4, 5]), Cons(1, Cons(2, Cons(3, Cons(4, Cons(5, None))))))
assert_equals(Cons.from_array([1, 2, 3, 4, 5]).to_array(),
              [1, 2, 3, 4, 5])

assert_equals(Cons.from_array([1, 2, 3, 4, 5])
              .filter(lambda n: n > 3)
              .to_array(), [4, 5])

assert_equals(Cons.from_array([1, 2, 3, 4, 5])
              .filter(lambda n: n > 5), None)

assert_equals(Cons.from_array(['1', '2', '3', '4', '5'])
              .map(int)
              .to_array(), [1, 2, 3, 4, 5])

assert_equals(Cons.from_array([1, 2, 3, 4, 5])
              .filter(lambda n: n % 2 == 0)
              .map(str)
              .to_array(), ['2', '4'])

assert_equals(Cons.from_array([1, 2, 3, 4]).zip(Cons.from_array([5, 6, 7, 8])),
              Cons((1, 5), Cons((2, 6), Cons((3, 7), Cons((4, 8), None)))))
