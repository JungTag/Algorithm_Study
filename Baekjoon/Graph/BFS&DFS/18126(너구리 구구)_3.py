# https://www.acmicpc.net/problem/18126
import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

def dfs(u, c):
    visited[u] = 1
    result = c
    for v, w in g[u]:
        if not visited[v]:
            result = max(result, dfs(v, c+w))
    return result

# init 
input = sys.stdin.readline
n = int(input().strip())
g = defaultdict(list)
visited = [0 for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    g[a].append([b, c])
    g[b].append([a, c])
print(dfs(1, 0))