import sys

class Queue:
    def __init__(self):
        self.items = []
        self.front_Index = 0
    def push(self, val):
        self.items.append(val)
    def pop(self):
        if len(self.items) == 0 or self.front_Index == len(self.items):
            print(-1)
        else:
            x = self.items[self.front_Index]
            self.front_Index += 1
            print(x)
    def front(self):
        if len(self.items) == 0 or self.front_Index == len(self.items):
            print(-1)
        else:
            x = self.items[self.front_Index]
            print(x)
    def back(self):
        if len(self.items) == 0 or self.front_Index == len(self.items):
            print(-1)
        else:
            x = self.items[len(self.items)-1]
            print(x)
    def size(self):
        return len(self.items) - self.front_Index
    def empty(self):
        if self.size() == 0:
            print(1)
        else:
            print(0)

my_Queue = Queue()
n = int(input())

for i in range(n):
    order = sys.stdin.readline().split()

    if order[0] == "push":
        value = int(order[1])
        my_Queue.push(value) 
    elif order[0] == "pop":
        my_Queue.pop()
    elif order[0] == "size":
        print(my_Queue.size())
    elif order[0] == "empty":
        my_Queue.empty()
    elif order[0] == "front":
        my_Queue.front()
    elif order[0] == "back":
        my_Queue.back()