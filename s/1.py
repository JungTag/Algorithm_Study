import sys
from collections import deque

def solve():
    q = deque([[2, 2, 1, 1]])
    g[1][1] = -1
    snake_len = 1
    sec = 0
    i = 1
    pi = 1

    while q:
        sec += 1
        hy, hx, ty, tx = q.popleft()

        if is_collision(hy, hx, snake_len):
            break
        else:
            if g[hy][hx] == 1:
                snake_len += 1
            else:
                g[ty][tx] = 0
                ty, tx = ty + d[i][1], tx + d[i][0]

        g[hy][hx] = -1
        
        if dirs:
            x, c = dirs[0]

        if sec == x:
            dirs.popleft()
            if c == "L":
                i -= 1
            else:
                i += 1
            i %= 4

        ny, nx = hy + d[i][1], hx + d[i][0]
        q.append([ny, nx, ty, tx])

    return sec

def is_collision(ny, nx, snake_len):
    if not(0<=ny<n+1 and 0<=nx<n+1):
        return True
    if snake_len != 1:
        if g[ny][nx] == -1:
            return True
    return False


# init
input = sys.stdin.readline
d = [[0, -1], [1, 0], [0, 1], [-1, 0]] # 상우하좌 오른쪽으로 꺾으면 +1, 왼쪽으로 꺾으면 -1

n = int(input().strip())
k = int(input().strip())
g = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(k):
    r, c = map(int, input().split())
    g[r][c] = 1
l = int(input().strip())
dirs = deque([[int(x) if i == 0 else x for i, x in enumerate(input().split())] for _ in range(l)])

print(solve())

