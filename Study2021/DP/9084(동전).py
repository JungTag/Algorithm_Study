# https://www.acmicpc.net/problem/9084
import sys

def get_number_of_cases():
    dp = [0 for _ in range(m+1)]
    dp[0] = 1
    for coin in coins:
        for i in range(coin, m+1):
            dp[i] += dp[i-coin]
    return dp[m]

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    coins = [int(x) for x in sys.stdin.readline().split()]
    m = int(sys.stdin.readline().strip())

    print(get_number_of_cases())