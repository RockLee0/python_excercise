#queue is a way of storing value through which you add value at first and when you exract a value, that is remove from the last

'''
{15,12,19} let's say you have put some values like these. when adding new element such as 20, this is added at the first
ex: {20,15,12,19}
and when access it, only the last value (first added value) is accessed. here in this case, 19
'''

# multiple ways you can store value in such structure

# one is using list

ticket_line=[]
ticket_line.insert(0,'shakil')
ticket_line.insert(0,'nayeem')
ticket_line.insert(0,'john')
print(ticket_line)

ticket_line.pop()
print(ticket_line)

# issue: list has a fixed size, when it overloads, it changes the position and put all the values again.whose time complexity is bad

# using deque
from collections import deque
q=deque()
q.appendleft('shalkil')
q.appendleft(15)
print(q)
q.pop()
print(q)

#making deque class
from collections import deque


class Queue:

    def __init__(self):
        self.buffer = deque() #remember that they use buffer

    def enqueue(self, val):
        self.buffer.appendleft(val)  #enqueue

    def dequeue(self):
        return self.buffer.pop()   #dequeue

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

pq = Queue()

pq.enqueue({
        'company': 'Wall Mart',
        'timestamp': '15 apr, 11.01 AM',
        'price': 131.10
    })
pq.enqueue({
        'company': 'Wall Mart',
        'timestamp': '15 apr, 11.02 AM',
        'price': 132
    })
pq.enqueue({
        'company': 'Wall Mart',
        'timestamp': '15 apr, 11.03 AM',
        'price': 135
    })


print(pq)