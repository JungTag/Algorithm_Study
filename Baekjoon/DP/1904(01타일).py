import sys

n = int(sys.stdin.readline().strip())
MOD = 15746

dp = [0 for _ in range(n+1)]
dp[1:3] = [1, 2]

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % MOD 

print(dp[n])