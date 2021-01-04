import sys

n = int(input())
p = [int(x) for x in sys.stdin.readline().split()]
p = [0] + p

dp = [0] * (n+1)
for i in range(1, n+1):
    dp[i] = p[i]

for i in range(1, n+1):
    for j in range(i-1, 0, -1):
        if j < i - j:
            break
        if dp[j] + dp[i-j] > dp[i]:
            dp[i] = dp[j] + dp[i-j]

print(dp[n])

