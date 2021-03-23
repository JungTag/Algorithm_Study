import sys
sys.setrecursionlimit(10**6)

def dfs(y, x):
    visited[y][x] = 1
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            if g[y][x] == g[ny][nx] and not visited[ny][nx]:
                dfs(ny, nx)

def cw_dfs(y, x):
    cw_visited[y][x] = 1
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            cur = g[y][x]
            if g[y][x] == g[ny][nx] and not cw_visited[ny][nx]:
                cw_dfs(ny, nx)
            elif g[y][x] != g[ny][nx] and not cw_visited[ny][nx]:
                if cur == 'G':
                    if g[ny][nx] == 'R':
                        cw_dfs(ny, nx)
                elif cur == 'R':
                    if g[ny][nx] == 'G':
                        cw_dfs(ny, nx)
    
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

n = int(sys.stdin.readline().strip())
g = [[x for x in sys.stdin.readline().strip()] for _ in range(n)]

visited = [[0 for _ in range(n)] for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            cnt += 1

cw_visited = [[0 for _ in range(n)] for _ in range(n)]
cw_cnt = 0
for i in range(n):
    for j in range(n):
        if not cw_visited[i][j]:
            cw_dfs(i, j)
            cw_cnt += 1

print(cnt, cw_cnt)