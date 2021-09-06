import sys
sys.setrecursionlimit(10**9)

def dfs(y, x, r):
    visited[y][x] = 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            if g[ny][nx] > r and not visited[ny][nx]:
                dfs(ny, nx,r)


dy = [1, 0, -1 , 0]
dx = [0, 1, 0, -1]
g = []
result = 1
MAX = float('-inf')
n = int(sys.stdin.readline().strip())

# input
for _ in range(n):
    _input = [int(x) for x in sys.stdin.readline().split()]
    _max = max(_input)
    if _max > MAX:
        MAX = _max
    g.append(_input)

# DFS
for i in range(1, MAX):
    visited = [[0]*n for _ in range(n)]
    cnt = 0
    for j in range(n):
        for k in range(n):
            if g[j][k] > i and not visited[j][k]:
                dfs(j, k, i)
                cnt += 1
    if cnt > result:
        result = cnt

print(result)