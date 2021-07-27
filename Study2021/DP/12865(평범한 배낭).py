# https://www.acmicpc.net/problem/12865
import sys

n, k = map(int, sys.stdin.readline().split())
bags = [[0, 0]] + [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)]
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    w, v = bags[i]
    for j in range(1, k+1):
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

print(dp[n][k])