import sys
sys.setrecursionlimit(10**9)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(y, x):
    visited[y][x] = 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < m:
            if not visited[ny][nx]:
                dfs(ny, nx)

t = int(sys.stdin.readline().strip())

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split()) # 가로, 세로, 위치
    visited = [[1 for _ in range(m)] for _ in range(n)]
    locs = []
    cnt = 0

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        visited[y][x] = 0
        locs.append([x, y])

    for loc in locs:
        x, y = loc
        if not visited[y][x]:
            dfs(y, x)
            cnt += 1
            
    print(cnt)
