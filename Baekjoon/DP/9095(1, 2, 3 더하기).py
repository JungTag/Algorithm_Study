import sys

t = int(sys.stdin.readline().strip())
dp = [0 for _ in range(12)]
dp[0:3] = [1, 1, 2]

for i in range(3, 12):
    for j in range(1, 4):
        dp[i] += dp[i-j]

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    print(dp[n])
