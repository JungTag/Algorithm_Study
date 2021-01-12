import sys

n, k = map(int, sys.stdin.readline().split())
coins = []
dp = [0 for _ in range(k+1)] 
dp[0] = 1

for _ in range(n):
    coins.append(int(sys.stdin.readline().strip()))

coins = list(set(coins)) # 중복 제거

for coin in coins:
    for i in range(1, k+1):
        if i - coin >= 0:
            dp[i] += dp[i-coin]

print(dp[k])