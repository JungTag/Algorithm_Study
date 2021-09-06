import sys

class Queue:
    def __init__(self):
        self.items = []
        self.front_Index = 0
    def push(self, val, i):
        x = []
        x.append(val); x.append(i)
        self.items.append(x)
    def pop(self):
        if len(self.items) == 0 or self.front_Index == len(self.items):
            return -1
        else:
            x = self.items[self.front_Index][0]
            self.front_Index += 1
            return x
    def front(self):
        if len(self.items) == 0 or self.front_Index == len(self.items):
            return -1
        else:
            x, y = self.items[self.front_Index][0], self.items[self.front_Index][1] 
            return x, y
    def size(self):
        return len(self.items) - self.front_Index
    def empty(self):
        return self.size() == 0


n = int(input())

for i in range(n):
    N, M = map(int,sys.stdin.readline().split())
    input_list = list(map(int,sys.stdin.readline().split()))
    cnt = 0 #출력 횟수
    importance_list = []
    my_Queue = Queue()
    
    for i in range(len(input_list)):
        my_Queue.push(input_list[i], i) #my_Queue.push(중요도, 입력 순서)
        importance = my_Queue.items[i][0] #importance = 중요도
        importance_list.append(importance) #중요도를 중요도 리스트에 저장!
    
    importance_list.sort() #중요도 오름차순으로 정렬!

    while not(my_Queue.empty()): #(***)my_Queue.size() == False -> 이렇게 하면 루프 안돎..!
        importance_to_extract, index_to_extract = my_Queue.items[M] #item = [value, index]의 형태이므로
        importance, index = my_Queue.front() #가장 앞에 있는 원소의 중요도와 입력 순서
        last = len(importance_list) - 1
        most_importance = importance_list[last] #오름차순으로 정렬되어있으므로 가장 마지막 인덱스가 가장 높은 중요도를 지님!

        # importance <= most_imptortance (importance > most_importace인 경우는 없음)
        if importance < most_importance: #중요도가 낮으므로 뒤로 옮긴다 
            my_Queue.push(my_Queue.pop(), index)
        else:
            if importance == importance_to_extract and index == index_to_extract: #중요도와 입력 순서가 모두 같은 원소에 접근했을 때
                my_Queue.pop()
                cnt += 1
                print(cnt)
                break
            else: #중요도는 같지만 입력 순서가 다른 원소에 접근했을 때(중요도는 같으므로 출력해줘야 함: cnt+=1)
                my_Queue.pop()
                cnt += 1
                importance_list.pop()
            


'''
딕셔너리 이용? -> 쓸 필요 X
문제: 
1) value가 같을 때 어떻게 구별할 것인가? -> 그냥 2차원 리스트 만들면 됨
2) 중요성 비교 -> 하나의 리스트를 더 만듦(더 좋은 방법 있을듯..?)
'''
