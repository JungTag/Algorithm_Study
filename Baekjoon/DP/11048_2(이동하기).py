# https://www.acmicpc.net/problem/11048
import sys

n, m = map(int, sys.stdin.readline().split())
g = [[0 for _ in range(m+1)]] + [[0]+[int(x) for x in sys.stdin.readline().split()] for _ in range(n)]
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = g[i][j] + max(dp[i-1][j], dp[i][j-1])

print(dp[n][m])