import sys

#입력은 무조건 sys.stdin으로 !!!
class Stack:
    def __init__(self):
        self.items=[]
    def push(self, value):
        self.items.append(value)
    def pop(self):
        try:
            print(self.items.pop())
        except IndexError:
            print(-1)
    def top(self):
        try:
            print(self.items[-1])
        except IndexError:
            print(-1)
    def size(self):
        print(len(self.items))
    def empty(self):
        if len(self.items) == 0:
            print(1)
        else:
            print(0)

my_Stack = Stack()
n = int(input())

for i in range(n):
    order = sys.stdin.readline().split()

    if order[0] == "push":
        value = int(order[1])
        my_Stack.push(value) 
    elif order[0] == "pop":
        my_Stack.pop()
    elif order[0] == "size":
        my_Stack.size()
    elif order[0] == "empty":
        my_Stack.empty()
    elif order[0] == "top":
        my_Stack.top()