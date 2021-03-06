import threading

N = 1000000
counter = 0
LOCK = threading.Lock()


def increment_thread():
    global counter
    for _ in range(N):
        with LOCK:
            counter += 1


t1 = threading.Thread(target=increment_thread)
t2 = threading.Thread(target=increment_thread)
t3 = threading.Thread(target=increment_thread)

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()

print(f"Counter value is {counter}")
