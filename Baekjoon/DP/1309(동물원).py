import sys

MOD = 9901

n = int(sys.stdin.readline().strip())

dp = [[0 for _ in range(3)] for _ in range(n)]
dp[0][0] = dp[0][1] = dp[0][2] = 1

for i in range(1, n):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % MOD
    dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % MOD
    dp[i][2] = sum(dp[i-1]) % MOD

print(sum(dp[n-1]) % MOD)