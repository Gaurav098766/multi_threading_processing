import time
from threading import Thread
from queue import Queue


def consumer(q):
    while True:
        txt = q.get()
        print(txt)
        time.sleep(1)


def producer(q):
    while True:
        q.put("Hello there")
        print("Message sent")
        time.sleep(1)

q = Queue()
t1 = Thread(target = consumer, args=(q,))
t2 = Thread(target = producer, args=(q,))
t1.start()
t2.start()