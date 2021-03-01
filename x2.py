import sys, collections, copy
sys.setrecursionlimit(10**6)

def bfs(s, visited):
    visited[s[0]][s[1]] = 1
    q = collections.deque([s])
    while q:
        y, x = q.popleft()
        if g[y][x] == 1:
            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                if 0 <= ny < n and 0 <= nx < m:
                    if g[ny][nx] and not visited[ny][nx]:
                        visited[ny][nx] = 1
                        q.append([ny, nx])
        elif g[y][x] == 2: # 가로
            for i in range(2):
                ny, nx = y+ry[i], x+rx[i]
                if 0 <= ny < n and 0 <= nx < m:
                    if (g[ny][nx] == 1 or g[ny][nx] == 2 or g[ny][nx] == 4) and not visited[ny][nx]:
                        visited[ny][nx] = 1
                        q.append([ny, nx])                
        elif g[y][x] == 3: # 세로
            for i in range(2):
                ny, nx = y+cy[i], x+cx[i]
                if 0 <= ny < n and 0 <= nx < m:
                    if (g[ny][nx] == 1 or g[ny][nx] == 3 or g[ny][nx] == 4) and not visited[ny][nx]:
                        visited[ny][nx] = 1
                        q.append([ny, nx])
        else:
            for i in range(4):
                ny, nx = y+dy[i], x+dx[i]
                if 0 <= ny < n and 0 <= nx < m:
                    if g[ny][nx] and not visited[ny][nx]:
                        visited[ny][nx] = 1
                        q.append([ny, nx])



def back_track(idx, depth, total):
    global result

    if idx >= LIMIT:
        return

    if depth >= isl-1:
        cnt = 0
        visited = copy.deepcopy(visited_org)
        for i in range(n):
            for j in range(m):
                if g[i][j] and not visited[i][j]:
                    if cnt == 0:
                        bfs([i, j], visited)
                        cnt += 1
                    else:
                        return
        result = min(result, total)
        return

    ay, ax, by, bx = cos[idx][0][0], cos[idx][0][1], cos[idx][1][0], cos[idx][1][1]
    dist = abs(ay - by) + abs(ax - bx) - 1
    if ay == by: # 가로로 다리 건설
        for i in range(ax+1, bx):
            if g[ay][i] == 0:
                g[ay][i] = 2
            elif g[ay][i] == 3:
                g[ay][i] = 4
        back_track(idx+1, depth+1, total+dist)        
        for i in range(ax+1, bx):
            if g[ay][i] == 2:
                g[ay][i] = 0
            elif g[ay][i] == 4:
                g[ay][i] = 3
    else: # 세로로 다리 건설
        for i in range(ay+1, by):
            if g[i][ax] == 0:
                g[i][ax] = 3
            elif g[i][ax] == 2:
                g[i][ax] = 4
        back_track(idx+1, depth+1, total+dist)       
        for i in range(ay+1, by):
            if g[i][ax] == 3:
                g[i][ax] = 0
            elif g[i][ax] == 4:
                g[ay][i] = 2
    back_track(idx+1, depth, total)
    

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
rx = [-1, 1]
ry = [0, 0]
cx = [0, 0]
cy = [-1, 1]

n, m = map(int, sys.stdin.readline().split())
g = [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)]

visited_org = [[0 for _ in range(m)] for _ in range(n)]
visited_isl = copy.deepcopy(visited_org)
cos = []
result = float('inf')
isl = 0

for i in range(n):
    for j in range(m):
        if g[i][j] and not visited_isl[i][j]:
            bfs([i, j], visited_isl)
            isl += 1

for i in range(n):
    for j in range(m-1):
        dist = 0
        if g[i][j]:
            for k in range(j+1, m):
                if not g[i][k]:
                    dist += 1
                elif g[i][k] and dist >= 2:
                    cos.append([[i,j], [i,k]])
                    break
                else:
                    break

for j in range(m):
    for i in range(n-1):
        dist = 0
        if g[i][j]:
            for k in range(i+1, n):
                if not g[k][j]:
                    dist += 1
                elif g[k][j] and dist >= 2:
                    cos.append([[i,j], [k,j]])
                    break
                else:
                    break

LIMIT = len(cos)
back_track(0, 0, 0)

if result == float('inf'):
    print(-1)
else:
    print(result)