import sys
sys.setrecursionlimit(10**9)

def dfs(y, x, d, state):
    global cnt
    
    if state: # if state == 1 -> 1번 / if state == 0 -> 2번
        visited[y][x] = 1
        cnt += 1

    nd = d

    for _ in range(4): # b
        nd = turn[nd]
        ny, nx = y + advance[nd][0], x + advance[nd][1]
        
        if not g[ny][nx] and not visited[ny][nx]: # a
            dfs(ny, nx, nd, 1)
            return
    
    ry, rx = y + regress[d][0], x + regress[d][1]

    if g[ry][rx]: # d
        return
    else:
        dfs(ry, rx, d, 0) # c

    
turn = {0: 3, 1: 0, 2: 1, 3: 2}
advance = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]} # [y,x]
regress = {0: [1, 0], 1: [0, -1], 2: [-1, 0], 3: [0, 1]}

n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())

cnt = 0
g = []
visited = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(n):
    raw = [int(x) for x in sys.stdin.readline().split()]
    g.append(raw)

dfs(r, c, d, 1)
print(cnt)