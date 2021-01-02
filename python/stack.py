class StackElement(object):
    def __init__(self, val):
        self._val = val
        self.next_ = None

    @property
    def value(self):
        return self._val


class Stack(object):
    """
    Implement a stack that has the following methods:

    - push(val), which pushes an element onto the stack
    - pop(), which pops off and returns the topmost element of the stack.
        If there are no elements in the stack, then it should throw an error or return None.
    - max(), which returns the maximum value in the stack currently. If there are no elements in the stack,
        then it should throw an error or return None.

    ** Each method should run in constant time. **
    """
    def __init__(self):
        self._head = None
        self._max = None
        self._count = 0

    def is_empty(self):
        return bool(self._head is None)

    def push(self, val):
        if not self._head:
            # Insert into the stack the element and the max val.
            self._head = StackElement((val, val))
            self._max = val
        else:
            tmp = self._head
            self._max = val if val > self._max else tmp.value[1]
            self._head = StackElement((val, self._max))
            self._head.next_ = tmp

        self._count += 1

    def pop(self):
        if not self._head:
            return None
        tmp = self._head
        self._head = self._head.next_
        val, _ = tmp.value
        if self._head:
            if val == self._max:
                # Max gets updated based on the current stack head
                self._max = self._head.value[1]

        self._count -= 1

        return val

    def max(self):
        return self._max if self._head else None

    def peek(self):
        # Top of the stack without removing it
        return self._head.value[0]

    @property
    def count(self):
        return self._count


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(3)
    assert s.max() == 3
    s.push(4)
    assert s.max() == 4
    assert s.pop() == 4
    assert s.max() == 3
    s.push(10)
    s.push(0)
    s.push(2)
    assert s.max() == 10
    # empty the stack
    assert s.pop() == 2
    assert s.pop() == 0
    assert s.max() == 10
    assert s.pop() == 10
    assert s.max() == 3
    assert s.pop() == 3
    assert s.pop() == 1
    assert s.pop() is None
    assert s.pop() is None
    assert s.max() is None
    s.push(0)
    assert s.max() == 0
    assert s.pop() == 0
    assert s.pop() is None
