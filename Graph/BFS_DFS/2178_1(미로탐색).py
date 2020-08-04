import sys
from collections import deque

'''
# 중요: Q에서 pop할 때 visit = True해주는 것이 아니라 Q에 append해줄 때 visit = True를 해야 중복방문을 피한다!
'''

n, m = map(int, sys.stdin.readline().split())
maze = []
maze.append([0 for _ in range(m+2)])
for _ in range(n):
    x = deque([int(x) for x in list(sys.stdin.readline().strip())])
    x.appendleft(0)
    x.append(0)
    maze.append(x)
maze.append([0 for i in range(m+2)])

visit = [[False] * (m+2) for _ in range(n+2)]
visit[1][1] = True
dist = [[0] * (m+2) for _ in range(n+2)]
dist[1][1] = 1  # 시작 위치(1,1)
Q = deque([])
Q.append([1,1]) # 시작 위치부터 탐색

while Q:
    v = Q.popleft()
    raw, col = v[0], v[1]
    if maze[raw-1][col] == 1 and visit[raw-1][col] == False:
        visit[raw-1][col] = True
        Q.append([raw-1,col])
        dist[raw-1][col] = dist[raw][col] + 1
    if maze[raw][col+1] == 1 and visit[raw][col+1] == False:
        visit[raw][col+1] = True
        Q.append([raw,col+1])
        dist[raw][col+1] = dist[raw][col] + 1
    if maze[raw+1][col] == 1 and visit[raw+1][col] == False:
        visit[raw+1][col] = True
        Q.append([raw+1,col])
        dist[raw+1][col] = dist[raw][col] + 1
    if maze[raw][col-1] == 1 and visit[raw][col-1] == False:
        visit[raw][col-1] = True
        Q.append([raw,col-1])
        dist[raw][col-1] = dist[raw][col] + 1
            
print(dist[n][m])
