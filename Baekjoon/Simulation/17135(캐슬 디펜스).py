import sys, itertools, collections, copy

dx = [-1, 0, 1]
dy = [0, -1, 0]

def bfs(y, x):
    q = collections.deque([[y, x, 1]])
    visited = set([(y, x)])

    while q:
        cy, cx, cd = q.popleft()
        if cd > d:
            return False
        if g[cy][cx]:
            return [cy, cx]
        for i in range(3):
            ny, nx = cy+dy[i], cx+dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if (ny, nx) not in visited:
                    visited.add((ny, nx))
                    q.append([ny, nx, cd+1])
    
n, m, d = map(int, sys.stdin.readline().split())
org_g= [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)]
MAX = float('-inf')

for combi in list(itertools.combinations(range(m), 3)):
    g = copy.deepcopy(org_g)
    targets = []
    cnt = 0

    for i in range(n-1, -1, -1):
        for j in combi:
            target = bfs(i, j)
            if target:
                targets.append(target)
        while targets:
            y, x = targets.pop()
            if g[y][x]:
                g[y][x] = 0
                cnt += 1

    MAX = max(MAX, cnt)

print(MAX)