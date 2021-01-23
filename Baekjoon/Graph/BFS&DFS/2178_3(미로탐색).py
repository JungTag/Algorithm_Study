import sys

'''
deque 안 쓰고 list로 했는데 시간이랑 메모리 줄어들음.. -> 주어진 list의 길이가 길지 않아서 그런듯?
'''

n, m = map(int, input().split())
maze = []
maze.append([0 for _ in range(m+2)])
for _ in range(n):
    x = [int(x) for x in list(sys.stdin.readline().strip())]
    x.insert(0,0)
    x.append(0)
    maze.append(x)
maze.append([0 for _ in range(m+2)])

visit = [[False] * (m+2) for _ in range(n+2)]
Q = []
distance_to_goal = 1

Q.append((1,1,1)) # 시작 위치부터 탐색, (x,y,distance)
while Q:
    v = Q.pop(0)
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
