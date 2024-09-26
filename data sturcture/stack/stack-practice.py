#take some values in a order and getting those values in reverse order.This type we need to be done as it is used in many type of websites or apps

#this feature can be done by storing data in list, but their is size limitation.
s=[]
s.append(5)
s.append(6)
s.append(8)
s.append(100)
print(s)

s.pop()
print(s)
print(s.pop()) #returns the poped value


#optimized usecase is using deque() class from collections (no size issue)
from collections import deque
stack=deque()
stack.append(4)
stack.append(9)
stack.append(10)
stack.append(15)
print('stacks are:',stack)

print(stack.pop()) #the popped item

print(stack)


#TASK

class Ptack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


#TASK 1


l=Ptack()
def reverse_string():
    s=input('what is your in your mind?')
    for i in s:
        l.push(i)
    result=''
    for j in range(l.size()):
        result=result+l.pop()
    return result
print(reverse_string())


#TASK 2

