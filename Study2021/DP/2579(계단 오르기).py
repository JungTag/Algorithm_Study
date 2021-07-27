# https://www.acmicpc.net/problem/2579
import sys

n = int(sys.stdin.readline().strip())
steps = [0, 0, 0] + [int(sys.stdin.readline().strip()) for _ in range(n)]
dp = [0 for _ in range(n+3)]

for i in range(3, n+3):
    dp[i] = max(dp[i-3]+steps[i-1], dp[i-2]) + steps[i]

print(dp[-1])