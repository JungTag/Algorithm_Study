import sys
n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
INF = float('inf')
G = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, cost = map(int, sys.stdin.readline().split())
    if G[a][b] > cost:
        G[a][b] = cost

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            G[i][j] = 0

'''
틀린 코드
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if G[i][j] > G[i][k] + G[k][j]:
                G[i][j] = G[i][k] + G[k][j]
'''
# 경유지(k)를 순회
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if G[i][j] > G[i][k] + G[k][j]:
                G[i][j] = G[i][k] + G[k][j]

for i in range(1, n+1):
    for j in range(1, n+1):
        if G[i][j] == INF:
            print(0, end=" ")
        else:
            print(G[i][j], end=" ")
    print()