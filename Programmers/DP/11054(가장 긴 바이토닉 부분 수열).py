import sys

n = int(sys.stdin.readline().strip())
a = [int(x) for x in sys.stdin.readline().split()]
dp = [[1 for _ in range(2)] for _ in range(n)]

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i][0] = max(dp[i][0], dp[j][0]+1)

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if a[i] > a[j]:
            dp[i][1] = max(dp[i][1], dp[j][1]+1)

dp = list(map(lambda x: x[0]+x[1], dp))
print(max(dp)-1)