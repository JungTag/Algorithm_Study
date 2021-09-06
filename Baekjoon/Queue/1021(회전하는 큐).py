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
            return self.items.pop()
        except IndexError:
            return -1
    def pop_front(self):
        try:
            return self.items.pop(0)
        except IndexError:
            return -1
    def back(self):
        try:
            return self.items[-1]
        except IndexError:
            return -1
    def front(self):
        try:
            return self.items[0]
        except IndexError:
            return -1
    def size(self):
        return len(self.items)
    def empty(self):
        if len(self.items) == 0:
            return 1
        else:
            return 0
    def shift_left(self):
        self.push_back(self.pop_front())
    def shift_right(self):
        self.push_front(self.pop_back())

my_Queue = Dequeue()

N, M = map(int,sys.stdin.readline().split())
pull_list = list(map(int,sys.stdin.readline().split())) #뽑아내려고 하는 원소들의 리스트
cnt = 0 #2번과 3번 연산의 횟수

for i in range(1, N+1):
    my_Queue.push_back(i) #큐의 크기인 N만큼 차례대로 숫자를 큐에 채워줌(1,2,3,...,N-1,N)

while True:
    front = my_Queue.front()
    m = my_Queue.size() // 2
    if front == pull_list[0]: #순서대로!! 뽑아야 하므로 맨 첫 번째 원소(pull_list[0])와 비교해줘야 한다. 
        pull_list.remove(my_Queue.pop_front()) 
        '''
        my_Queue.pop_front()
        pull_list.pop(0)해도 됨! (front == pull_list[0]이니깐)
        '''
        if not pull_list: #뽑아내야 할 원소들의 리스트가 비었다면? break한다.
            break
    else:
        if pull_list[0] in my_Queue.items[:m+1]: #큐를 반으로 나누었을 때 뽑아내야 하는 원소가 앞쪽에 있을 때
            my_Queue.shift_left()
            cnt += 1
        else:
            my_Queue.shift_right() #큐를 반으로 나누었을 때 뽑아내야 하는 원소가 뒤쪽에 있을 때
            cnt += 1

print(cnt)
            
    

