# https://www.acmicpc.net/problem/7576
import sys
import collections

def bfs():
    global unripe_cnt
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    while queue:
        y, x, day = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if g[ny][nx] == 0:
                    g[ny][nx] = 1
                    queue.append([ny, nx, day+1])
                    unripe_cnt -= 1
    if unripe_cnt:
        return(-1)
    else:
        return(day)    

g = []
queue = collections.deque([])
unripe_cnt = 0

m, n = map(int, sys.stdin.readline().split())
for i in range(n):
    raw = [int(x) for x in sys.stdin.readline().split()]
    for j, x in enumerate(raw):
        if x == 0: 
            unripe_cnt += 1
        elif x == 1:
            queue.append([i, j, 0])
    g.append(raw)

print(bfs())