import sys
n = int(input())
map_list = []
map_list.append([0 for i in range(n+2)])
for i in range(n):
    x = [int(x) for x in list(sys.stdin.readline().strip())]
    x.insert(0,0)
    x.append(0)
    map_list.append(x)
map_list.append([0 for i in range(n+2)])

visit = []
for i in range(n+2):
    x = []
    for j in range(n+2):
        x.append(False)
    visit.append(x)

div_list = []
cnt = 1

def DFS_Graph(G):
    global cnt
    for i in range(1, n+1):
        for j in range(1, n+1):
            if visit[i][j] == False and G[i][j] == 1:
                DFS(i,j)
                div_list.append(cnt) 
                cnt = 1


def DFS(i,j):   
    visit[i][j] = True
    global cnt 
    if map_list[i][j+1] == 1:
        if visit[i][j+1] == False:
            cnt += 1
            DFS(i, j+1)
    if map_list[i+1][j] == 1:
        if visit[i+1][j] == False:
            cnt += 1
            DFS(i+1, j)
    if map_list[i][j-1] == 1:
        if visit[i][j-1] == False:
            cnt += 1
            DFS(i, j-1)
    if map_list[i-1][j] == 1:
        if visit[i-1][j] == False:
            cnt += 1
            DFS(i-1, j)


DFS_Graph(map_list)
div_list.sort()
print(len(div_list))
for x in div_list:
    print(x)


# 인접을 어떻게 파악할 것인가?
# stack = []
# def DFS(s):
#     stack.append(s)
#     while len(stack) != 0:
#         v = stack.pop()
#         if visit[v] == False:
#             visit[v] = True
#             # for each edge(v,w):
#                 if visit[w] == False:
#                     stack.append(w)
