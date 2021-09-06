# https://www.acmicpc.net/problem/18405
import sys
from collections import deque

def solve():
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    while queue:
        w, y, x, sec = queue.popleft()
        if sec >= s:
            break
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if g[ny][nx] == 0:
                    g[ny][nx] = w
                    queue.append([w, ny, nx, sec+1])
    return g[dist_x-1][dist_y-1]


input = sys.stdin.readline
n, k = map(int, input().split())
g = []
starts = []
for i in range(n):
    raw = [int(x) for x in input().split()]
    for j, v in enumerate(raw):
        if v != 0:
            starts.append([v, i, j, 0])
    g.append(raw)
s, dist_x, dist_y = map(int, input().split())

queue = deque(sorted(starts))
print(solve())