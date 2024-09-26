#task  1::

from collections import deque
import time
import threading

class Queue:

    def __init__(self):
        self.buffer = deque() #remember that they use buffer

    def enqueue(self, val):
        for i in range(len(val)):
         time.sleep(0.5)
         self.buffer.appendleft(val)  #enqueue

    def dequeue(self):
        time.sleep(2)
        return self.buffer.pop()   #dequeue

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

pq = Queue()

orders = ['pizza','samosa','pasta','biryani','burger']

place=threading.Thread(pq.enqueue() , args=(orders,))
serve=threading.Thread(pq.dequeue())


place.start()
time.sleep(1)
serve.start()


place.join()
serve.join()


'''
different approach:
def place_orders(orders):
    for order in orders:
        print("Placing order for:",order)
        food_order_queue.enqueue(order)
        time.sleep(0.5)


def serve_orders():
    time.sleep(1)
    while True:
        order = food_order_queue.dequeue()
        print("Now serving: ",order)
        time.sleep(2)

'''