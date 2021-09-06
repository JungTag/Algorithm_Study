import sys

class Dequeue:
    def __init__(self):
        self.items = []
    def push_back(self, v):
        self.items.append(v)
    def push_front(self, v):
        self.items.insert(0, v)
    def pop_back(self):
        try:
            print(self.items.pop())
        except IndexError:
            print(-1)
    def pop_front(self):
        try:
            print(self.items.pop(0))
        except IndexError:
            print(-1)
    def back(self):
        try:
            print(self.items[-1])
        except IndexError:
            print(-1)
    def front(self):
        try:
            print(self.items[0])
        except IndexError:
            print(-1)
    def size(self):
        print(len(self.items))
    def empty(self):
        if len(self.items) == 0:
            print(1)
        else:
            print(0)


my_Queue = Dequeue()
n = int(input())

for i in range(n):
    order = sys.stdin.readline().split()

    if order[0] == "push_front":
        value = int(order[1])
        my_Queue.push_front(value)
    elif order[0] == "push_back":
        value = int(order[1])
        my_Queue.push_back(value) 
    elif order[0] == "pop_front":
        my_Queue.pop_front()
    elif order[0] == "pop_back":
        my_Queue.pop_back()
    elif order[0] == "size":
        my_Queue.size()
    elif order[0] == "empty":
        my_Queue.empty()
    elif order[0] == "front":
        my_Queue.front()
    elif order[0] == "back":
        my_Queue.back()