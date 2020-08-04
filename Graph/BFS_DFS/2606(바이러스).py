import sys
num_of_v = int(input())
n = int(input())

input_list = []
for i in range(n):
    input_list.append([int(x) for x in sys.stdin.readline().strip().split()])

# 그래프 초기화(인접행렬)
G = []
for i in range(num_of_v + 1):
    x = []
    for i in range(num_of_v +1):
        x.append(0)
    G.append(x)

# 엣지에 1할당
for x,y in input_list:
    G[x][y] = 1
    G[y][x] = 1

visit = [] # 방문한 노드를 기록하는 리스트
for v in range(num_of_v + 1):
    visit.append(False)

def DFS(v):
    visit[v] = True
    for w in range(1, num_of_v + 1):
        if G[v][w] == 1:
            if visit[w] == False:
                DFS(w)

DFS(1)
print(visit.count(True) - 1)