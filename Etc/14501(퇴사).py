import sys

n = int(sys.stdin.readline().strip())
pairs = [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)] #(t, p)

dp = [0 for _ in range(n+1)]

for i in range(n):
    time, pay = pairs[i]
    dp[i] = max(dp[i], dp[i-1])
    if i+time <= n:
        dp[i+time] = max(dp[i+time], dp[i]+pay)

print(max(dp))