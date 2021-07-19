# https://www.acmicpc.net/problem/1939
import sys
from collections import defaultdict, deque

def search():
    left, right = 1, max_c
    result = 1
    while left <= right:
        mid = (left+right) // 2
        if bfs(mid):
            result = mid
            left = mid+1
        else:
            right = mid-1
    return result

def bfs(target):
    visited = [0 for _ in range(n+1)]
    visited[start] = 1
    queue = deque([start])
    while queue:
        u = queue.popleft()
        if u == end:
            return True
        for v, w in g[u]:
            if not visited[v] and w >= target:
                visited[v] = 1
                queue.append(v)
    return False

# init
n, m = map(int, sys.stdin.readline().split())
g = defaultdict(list)
max_c = float('-inf')
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    g[a].append([b, c])
    g[b].append([a, c])
    max_c = max(max_c, c)
start, end = map(int, sys.stdin.readline().split())
print(search())