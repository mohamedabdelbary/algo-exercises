class QueueElement(object):
    def __init__(self, val):
        self._value = val
        self._next = None

    def add_next(self, elem):
        self._next = elem

    @property
    def value(self):
        return self._value

    @property
    def next_(self):
        return self._next


class Queue(object):
    """
    Implement a queue using. Recall that a queue is a FIFO (first-in, first-out) data structure
    with the following methods: enqueue(element), which inserts an element into the queue, and dequeue(),
    which removes it.
    both methods need to be performed in O(1) time
    """
    def __init__(self):
        self._size = 0
        self._head = None
        self._last = None

    def enqueue(self, element):
        if not self._head:
            self._head = QueueElement(element)
            self._last = self._head
        else:
            self._last.add_next(QueueElement(element))
            self._last = self._last.next_

        self._size += 1

    def dequeue(self):
        if not self._head:
            return None

        tmp = self._head
        self._head = tmp.next_
        self._size -= 1
        return tmp.value

    @property
    def head(self):
        return self._head.value if self._head else None

    @property
    def size(self):
        return self._size


if __name__ == '__main__':
    q = Queue()
    q.enqueue(10)
    q.enqueue(4)
    assert q.head == 10
    q.enqueue(7)
    assert q.dequeue() == 10
    assert q.size == 2
    q.enqueue(-1)
    assert q.head == 4
    assert q.dequeue() == 4
    assert q.size == 2
    assert q.head == 7
    q.dequeue()
    assert q.size == 1
    assert q.dequeue() == -1
    assert q.size == 0
    assert q.dequeue() is None
    assert q.head is None
    assert q.size == 0
