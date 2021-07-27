# https://www.acmicpc.net/problem/11657
import sys
from collections import defaultdict

def solve():
    INF = float('inf')
    dist = [INF for _ in range(n+1)]
    dist[1] = 0

    for _ in range(n-1):
        for u in range(1, n+1):
            for v, w in g[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

    for u in range(1, n+1): # check cycle
        for v, w in g[u]:
            if dist[u] + w < dist[v]:
                print(-1)
                return
    
    for i in range(2, n+1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])


input = sys.stdin.readline
n, m = map(int, input().split())
g = defaultdict(list)

for _ in range(m):
    a, b, c = map(int, input().split())
    g[a].append([b, c])

solve()