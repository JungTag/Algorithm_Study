import sys
from collections import deque

'''
메모리를 줄이려고 했는데, 오히려 메모리는 안 줄어들고 시간이 줄어들었다.
'''

n, m = map(int, input().split())
maze = []
maze.append([0 for _ in range(m+2)])
for _ in range(n):
    x = deque([int(x) for x in list(sys.stdin.readline().strip())])
    x.appendleft(0)
    x.append(0)
    maze.append(x)
maze.append([0 for _ in range(m+2)])

visit = [[False] * (m+2) for _ in range(n+2)]
Q = deque([])
distance_to_goal = 1

Q.append((1,1,1)) # 시작 위치부터 탐색, (x,y,distance)
while Q:
    v = Q.popleft()
    raw, col, dist = v[0], v[1], v[2]
    if raw == n and col == m:
        distance_to_goal = dist
        break
    if maze[raw-1][col] == 1 and visit[raw-1][col] == False:
        visit[raw-1][col] = True
        Q.append((raw-1,col,dist+1))
    if maze[raw][col+1] == 1 and visit[raw][col+1] == False:
        visit[raw][col+1] = True
        Q.append((raw,col+1,dist+1))
    if maze[raw+1][col] == 1 and visit[raw+1][col] == False:
        visit[raw+1][col] = True
        Q.append((raw+1,col,dist+1))
    if maze[raw][col-1] == 1 and visit[raw][col-1] == False:
        visit[raw][col-1] = True
        Q.append((raw,col-1,dist+1))

print(distance_to_goal)
