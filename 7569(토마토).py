import sys, collections

def bfs():
    result = 0
    q = collections.deque([])

    for co in ripe:
        z, y, x = co
        q.append([z, y, x, 0])

    while q:
        z, y, x, d = q.popleft()
        result = d

        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nz < k and 0 <= ny < n and 0 <= nx < m:
                if g[nz][ny][nx] == 0:
                    g[nz][ny][nx] = 1
                    q.append([nz, ny, nx, d+1])

    return result

dx = [0, 1, 0, -1, 0, 0]
dy = [-1, 0, 1, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

m, n, k = map(int, sys.stdin.readline().split())

g = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(k)]
ripe = []
empty = []
days = float('inf')

for z in range(k):
    for y in range(n):
        g[z][y] = [int(x) for x in sys.stdin.readline().split()]
        for x in range(m):
            if g[z][y][x] == 1:
                ripe.append([z, y, x])
            if g[z][y][x] == 0:
                empty.append([z, y, x])

days = bfs()

for co in empty:
    z, y, x = co
    if g[z][y][x] == 0:
        days = -1
        break

print(days)