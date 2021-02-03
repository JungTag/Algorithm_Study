import sys
sys.setrecursionlimit(10**9)

def paint(y1, x1, y2, x2):
    for i in range(y1, y2):
        for j in range(x1, x2):
            if not g[i][j]:
                g[i][j] = 1

def dfs(y, x, s):
    visited[y][x] = 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < m and 0 <= nx < n:
            if not visited[ny][nx] and not g[ny][nx]:
               s = dfs(ny, nx, s+1)

    return s

m, n, k = map(int, sys.stdin.readline().split())

g = [[0 for _ in range(n)] for _ in range(m)]
visited = [[0 for _ in range(n)] for _ in range(m)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0 ,-1]

cnt = 0
result = []

for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    paint(y1, x1, y2, x2)

for i in range(m):
    for j in range(n):
        if not g[i][j] and not visited[i][j]:
            result.append(dfs(i, j, 1))
            cnt += 1

print(cnt)
print(*sorted(result))