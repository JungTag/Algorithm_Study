# https://www.acmicpc.net/problem/11048
import sys

n, m = map(int, sys.stdin.readline().split())
g = [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]
dp[0][0] = g[0][0]

for i in range(1, n):
    dp[i][0] = g[i][0] + dp[i-1][0]
for j in range(1, m):
    dp[0][j] = g[0][j] + dp[0][j-1]

for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = g[i][j] + max(dp[i-1][j], dp[i][j-1])

print(dp[n-1][m-1])