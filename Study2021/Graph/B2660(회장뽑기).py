import sys
from collections import deque, defaultdict
# https://www.acmicpc.net/problem/2660

def bfs(start):
    queue = deque([[start, 0]])
    while queue:
        u, dist = queue.popleft()
        for v in g[u]:
            if not visited[v]:
                queue.append([v, dist+1])
                visited[v] = dist+1

def get_max_dist():
    max_dist = float('-inf')
    for dist in visited:
        if dist > max_dist:
            max_dist = dist
    return max_dist

n = int(sys.stdin.readline().strip())
g = defaultdict(list)
while True:
    a, b = map(int, sys.stdin.readline().split())
    g[a].append(b)
    g[b].append(a)
    if a == -1 and b == -1:
        break

result = defaultdict(int) # result = {회장후보: 점수}
for i in range(1, n+1):
    visited = [0 for _ in range(n+1)]
    visited[i] = 1
    bfs(i)
    result[i] = get_max_dist()

min_dist = min(result.values())
candis = [i for i, dist in result.items() if dist == min_dist]

print(min_dist, len(candis))
print(*candis) # 이미 입력순으로 정렬되어 있음