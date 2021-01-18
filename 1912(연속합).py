import sys

n = int(sys.stdin.readline().strip())
dp = [0] + [int(x) for x in sys.stdin.readline().split()]

for i in range(1, n+1):
    dp[i] = max(dp[i-1]+dp[i], dp[i])

print(max(dp[1:]))