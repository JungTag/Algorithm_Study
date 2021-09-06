import sys

def bfs(cur):
    global result
    cnt = 0
    if cur == len(cctv_cos):
        for i in range(n):
            for j in range(m):
                if g[i][j] == 0:
                    cnt += 1
        result = min(result, cnt)
        return
    for i in range(4):
        changed_cos = paint_graph(cur, i)
        bfs(cur + 1)
        for y, x in changed_cos:
            g[y][x] = 0

                    
def paint_graph(cur, dir):
    changed_cos = []
    cy, cx = cctv_cos[cur][0], cctv_cos[cur][1]

    if g[cy][cx] == 1:
        y, x = cy, cx
        while True:
            ny, nx = y + dy[dir], x + dx[dir]
            if 0 <= nx < m and 0 <= ny < n and g[ny][nx] != 6:
                if g[ny][nx] == 0:
                    g[ny][nx] = -1
                    changed_cos.append([ny, nx])
                y, x = ny, nx
            else:
                break
    elif g[cy][cx] == 2:
        for i in range(0, 3, 2):
            y, x = cy, cx
            while True:
                ny, nx = y + dy[(dir+i) % 4], x + dx[(dir+i) % 4]
                if 0 <= nx < m and 0 <= ny < n and g[ny][nx] != 6:
                    if g[ny][nx] == 0:
                        g[ny][nx] = -1
                        changed_cos.append([ny, nx])
                    y, x = ny, nx
                else:
                    break
    elif g[cy][cx] == 3:
        for i in range(2):
            y, x = cy, cx
            while True:
                ny, nx = y + dy[(dir+i) % 4], x + dx[(dir+i) % 4]
                if 0 <= nx < m and 0 <= ny < n and g[ny][nx] != 6:
                    if g[ny][nx] == 0:
                        g[ny][nx] = -1
                        changed_cos.append([ny, nx])
                    y, x = ny, nx
                else:
                    break
    elif g[cy][cx] == 4:
        for i in range(3):
            y, x = cy, cx
            while True:
                ny, nx = y + dy[(dir+i) % 4], x + dx[(dir+i) % 4]
                if 0 <= nx < m and 0 <= ny < n and g[ny][nx] != 6:
                    if g[ny][nx] == 0:
                        g[ny][nx] = -1
                        changed_cos.append([ny, nx])
                    y, x = ny, nx
                else:
                    break
    elif g[cy][cx] == 5:
        for i in range(4):
            y, x = cy, cx
            while True:
                ny, nx = y + dy[(dir+i) % 4], x + dx[(dir+i) % 4]
                if 0 <= nx < m and 0 <= ny < n and g[ny][nx] != 6:
                    if g[ny][nx] == 0:
                        g[ny][nx] = -1
                        changed_cos.append([ny, nx])
                    y, x = ny, nx
                else:
                    break                
                
    return changed_cos


input = sys.stdin.readline
n, m = map(int, input().split())
g = [[int(x) for x in input().split()] for _ in range(n)]
cctv_cos = []

for i in range(n):
    for j in range(m):
        if 1 <= g[i][j] <= 5:
            cctv_cos.append([i, j])

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

result = float('inf')

bfs(0)
print(result)