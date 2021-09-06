# https://www.acmicpc.net/problem/18126
import sys
from collections import defaultdict, deque

def bfs():
    visited = [0 for _ in range(n+1)]
    visited[1] = 1
    queue = deque([[1, 0]]) # node, cost
    result = 0
    while queue:
        u, c = queue.popleft()
        result = max(result, c)
        for v, w in g[u]:
            if not visited[v]:
                visited[v] = 1
                queue.append([v, c+w])
    return result

# init 
input = sys.stdin.readline
n = int(input().strip())
g = defaultdict(list)
for _ in range(n-1):
    a, b, c = map(int, input().split())
    g[a].append([b, c])
    g[b].append([a, c])

print(bfs())