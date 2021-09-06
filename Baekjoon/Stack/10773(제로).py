import sys

#입력은 무조건 sys.stdin으로 !!!
class Stack:
    def __init__(self):
        self.items=[]
    def push(self, value):
        self.items.append(value)
    def pop(self):
        self.items.pop()


my_Stack = Stack()
K = int(input()) #반복 횟수

for i in range(K):
    number = int(sys.stdin.readline().strip()) # 여러 번 입력받을 땐 꼭 sys.stdin.readline()
    if number == 0:
        my_Stack.pop()
    else:
        my_Stack.push(number)

sum = 0
for element in my_Stack.items:
    sum += element
print(sum)

'''
K가 10만일 경우, 입력 작업이 10만회 반복,
따라서 number = int(input())으로 하면 시간초과가 일어날 수 있음!
ex) 10828번
반복되는 입력은 무조건 sys.stdin.readline()을 쓰자!
'''



