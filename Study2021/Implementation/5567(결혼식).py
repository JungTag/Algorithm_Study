# https://www.acmicpc.net/problem/5567
import sys
from collections import defaultdict, deque

def bfs(start):
    cnt = 0
    visited = [0 for _ in range(n+1)]
    visited[start] = 1
    queue = deque([[start, 0]])
    while queue:
        u, dist = queue.popleft()
        if dist <= 2: # 친구의 친구(dist==2)까지 초대할 수 있다
            cnt += 1
        for v in g[u]:
            if not visited[v]:
                visited[v] = 1
                queue.append([v, dist+1])
    return cnt-1 # cnt에 자기 자신까지 포함되어 있으므로 1을 빼준다

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
g = defaultdict(list)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    g[a].append(b)
    g[b].append(a)

print(bfs(1))
