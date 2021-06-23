# https://www.acmicpc.net/problem/2178
import sys
import collections

def bfs():
    queue = collections.deque([[0, 0, 1]])
    while queue:
        y, x, dist = queue.popleft()
        if y == n-1 and x == m-1:
            return dist
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if g[ny][nx] and not visited[ny][nx]:
                    visited[ny][nx] = 1
                    queue.append([ny, nx, dist+1])

n, m = map(int, sys.stdin.readline().split())
g = [[int(x) for x in sys.stdin.readline().strip()] for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

print(bfs())