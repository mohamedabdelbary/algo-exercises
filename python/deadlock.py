"""
Write a simple program that deadlocks.
"""
from threading import RLock, Thread


class Deadlock:
    def __init__(self):
        self._lock1 = RLock()
        self._lock2 = RLock()

    def a(self):
        with self._lock1:
            print(f"Finished holding lock 1 in method a")
            with self._lock2:
                print(f"Finished holding lock 2 in method a")

    def b(self):
        with self._lock2:
            print(f"Finished holding lock 2 in method b")
            with self._lock1:
                print(f"Finished holding lock 1 in method b")


for i in range(1000):
    d = Deadlock()
    print(f"Iteration: {i}")
    t1 = Thread(target=d.a)
    t2 = Thread(target=d.b)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("===============")
