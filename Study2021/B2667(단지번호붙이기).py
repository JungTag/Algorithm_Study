# https://www.acmicpc.net/problem/2667
import sys
import collections
sys.setrecursionlimit(10**6)

def dfs(y, x, cnt):
    visited[y][x] = 1
    cnt += 1
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            if g[ny][nx] and not visited[ny][nx]:
                cnt = dfs(ny, nx, cnt)
    return cnt

n = int(sys.stdin.readline().strip())
g = [[int(x) for x in sys.stdin.readline().strip()] for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
results = []
complex = 0

for i in range(n):
    for j in range(n):
        if g[i][j] and not visited[i][j]:
            results.append(dfs(i, j, 0))
            complex += 1

print(complex)
for result in sorted(results):
    print(result)