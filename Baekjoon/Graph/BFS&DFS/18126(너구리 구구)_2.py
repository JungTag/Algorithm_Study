# https://www.acmicpc.net/problem/18126
import sys
from collections import defaultdict

def dfs():
    visited = [0 for _ in range(n+1)]
    visited[1] = 1
    stack = [[1, 0]] # node, cost
    result = 0
    while stack:
        u, c = stack.pop()
        result = max(result, c)
        for v, w in g[u]:
            if not visited[v]:
                visited[v] = 1
                stack.append([v, c+w])
    return result

# init 
input = sys.stdin.readline
n = int(input().strip())
g = defaultdict(list)
for _ in range(n-1):
    a, b, c = map(int, input().split())
    g[a].append([b, c])
    g[b].append([a, c])

print(dfs())