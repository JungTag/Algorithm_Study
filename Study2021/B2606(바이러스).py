# https://www.acmicpc.net/problem/2606
import sys
import collections
sys.setrecursionlimit(10**6)

def dfs(v):
    global cnt
    visited[v] = 1
    cnt += 1
    for w in g[v]:
        if not visited[w]:
            dfs(w)

n = int(sys.stdin.readline().strip())
num_of_edges = int(sys.stdin.readline().strip())
g = collections.defaultdict(list)
visited = [0 for _ in range(n+1)]
cnt = 0

for _ in range(num_of_edges):
    u, v = map(int, sys.stdin.readline().split())
    g[u].append(v)
    g[v].append(u)

dfs(1)
print(cnt-1)
