# https://www.acmicpc.net/problem/11404
import sys

def solve():
    for m in range(1, n+1):
        for u in range(1, n+1):
            for v in range(1, n+1):
                g[u][v] = min(g[u][v], g[u][m] + g[m][v])
    for i in range(1, n+1):
        for j in range(1, n+1):
            if g[i][j] == INF:
                print(0, end=" ")
            else:
                print(g[i][j], end=" ")
        print()


input = sys.stdin.readline
n = int(input().strip())
m = int(input().strip())
INF = float('inf')
g = [[INF for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    if c < g[a][b]:
        g[a][b] = c

for i in range(n+1):
    for j in range(n+1):
        if i == j:
            g[i][j] = 0

solve()