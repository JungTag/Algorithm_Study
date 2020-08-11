import sys
from collections import deque
N, K = map(int,sys.stdin.readline().split())

Q = deque([])
Q.append((N,0))
visited_point = {i:False for i in range(100001)}
visited_point[N] = True

while Q:
    top = Q.popleft()
    point, seconds = top[0], top[1]
    way1, way2, way3 = point-1, point+1, point*2
    if point == K:
        print(seconds)
        break
    if way1 == K or way2 == K or way3 == K:
        print(seconds+1)
        break
    if way1 >= 0 and visited_point[way1] == False:
        visited_point[way1] = True
        Q.append((way1, seconds+1))
    if way2 <= 100000 and visited_point[way2] == False:
        visited_point[way2] = True
        Q.append((way2, seconds+1))
    if way3 <= 100000 and visited_point[way3] == False:
        visited_point[way3] = True
        Q.append((way3, seconds+1))
