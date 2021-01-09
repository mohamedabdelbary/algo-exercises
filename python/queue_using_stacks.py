from stack import Stack


class Queue(object):
    """
    Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure
    with the following methods: enqueue(element), which inserts an element into the queue, and dequeue(),
    which removes it.
    """
    def __init__(self):
        self._tmp_stack = Stack()
        self._queue_stack = Stack()
        self._count = 0

    def enqueue(self, element):
        """
        - If the queue stack is empty, then empty the tmp stack
        into it.
        - Otherwise push the new element onto the tmp stack
        """
        self._tmp_stack.push(element)
        if self._queue_stack.is_empty():
            self._move_stack(self._tmp_stack, self._queue_stack)

        self._count += 1

    def dequeue(self):
        """
        Always dequeue from the queue stack
        """
        if self._queue_stack.is_empty():
            if not self._tmp_stack.is_empty():
                self._move_stack(self._tmp_stack, self._queue_stack)
                self._count -= 1
                return self._queue_stack.pop()
            else:
                return None
        else:
            self._count -= 1
            return self._queue_stack.pop()

    @property
    def head(self):
        if not self._queue_stack.is_empty():
            return self._queue_stack.peek()
        elif not self._tmp_stack.is_empty():
            self._move_stack(self._tmp_stack, self._queue_stack)
            return self._tmp_stack.peek()
        else:
            return None

    @property
    def count(self):
        return self._count

    @staticmethod
    def _move_stack(from_, to):
        while not from_.is_empty():
            to.push(from_.pop())


if __name__ == '__main__':
    q = Queue()
    q.enqueue(10)
    q.enqueue(4)
    assert q.head == 10
    q.enqueue(7)
    assert q.dequeue() == 10
    assert q.count == 2
    q.enqueue(-1)
    assert q.head == 4
    assert q.dequeue() == 4
    assert q.count == 2
    assert q.head == 7
    q.dequeue()
    assert q.count == 1
    assert q.dequeue() == -1
    assert q.count == 0
    assert q.dequeue() is None
    assert q.head is None
    assert q.count == 0
