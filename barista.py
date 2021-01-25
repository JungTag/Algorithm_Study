import sys, collections




tree = collections.defaultdict(list)
INF = float('inf')

n = int(sys.stdin.readline().strip())

dp = [[INF for _ in range(n+1)] for _ in range(n+1)]
for _ in range(n):
    u, v, d = map(int, sys.stdin.readline().split())
    tree[u].append(v)

