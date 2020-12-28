import sys
from collections import deque

'''
2<= M,N <= 1000 
디큐를 썼더니 해결
'''
M, N = map(int, sys.stdin.readline().split())
box = []
Q = deque([])
cnt = 0
box.append([-1 for _ in range(M+2)]) #len(box)-1
for i in range(1, N+1):
    inner_list = deque([int(x) for x in list(sys.stdin.readline().split())])
    for j in range(len(inner_list)):
        if inner_list[j] == 1:
            Q.append((i,j+1,0))
        if inner_list[j] == 0:
            cnt += 1
    inner_list.appendleft(-1)
    inner_list.append(-1)
    box.append(inner_list)
box.append([-1 for _ in range(M+2)])

check_cnt = 0
while Q:
    v = Q.popleft()
    raw, col, day = v[0], v[1], v[2]
    if box[raw-1][col] == 0:
        box[raw-1][col] = 1
        check_cnt += 1
        Q.append((raw-1,col,day+1))
    if box[raw][col+1] == 0:
        box[raw][col+1] = 1
        check_cnt += 1
        Q.append((raw,col+1,day+1))
    if box[raw+1][col] == 0:
        box[raw+1][col] = 1
        check_cnt += 1
        Q.append((raw+1,col,day+1))
    if box[raw][col-1] == 0:
        box[raw][col-1] = 1
        check_cnt += 1
        Q.append((raw,col-1,day+1))
    if not Q:
        if cnt == check_cnt:
            print(day)
        else:
            print(-1)

