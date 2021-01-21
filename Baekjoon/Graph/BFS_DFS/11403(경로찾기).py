import sys
sys.setrecursionlimit(10**6)

def dfs(start, cur):
    visited[cur] = 1
    if start != cur:
        path[start][cur] = 1

    for u in range(n):
        if u != cur and g[cur][u] and not visited[u]:
            dfs(start, u)
        if u == start and g[cur][u]:
            path[start][start] = 1


n = int(sys.stdin.readline().strip())
g = []
path = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(n):
    raw = [int(x) for x in sys.stdin.readline().split()]
    g.append(raw)

for i in range(n):
    visited = [0 for _ in range(n)]
    dfs(i, i)            

for raw in path:
    print(*raw)


