# https://www.acmicpc.net/problem/1753
import sys, heapq as hq
from collections import defaultdict

def solve():
    INF = float('inf')
    dist = [INF for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    dist[k] = 0
    queue = [[0, k]]

    while queue:
        c, u = hq.heappop(queue)
        visited[u] = 1
        for v, w in g[u]:
            if not visited[v] and c + w < dist[v]:
                dist[v] = c + w
                hq.heappush(queue, [dist[v], v])

    for i in range(1, n+1):
        if dist[i] == INF:
            print('INF')
        else:
            print(dist[i])


input = sys.stdin.readline
n, e = map(int, input().split())
k = int(input().strip())
g = defaultdict(list)
for _ in range(e):
    u, v, w = map(int, input().split())
    g[u].append([v, w])

solve()