import sys

n = int(input())
tri = []
for i in range(n):
    val = list(map(int, input().strip().split()))
    tri.append(val)

dp = []
for i in range(n):
    new = []
    for j in range(0, i+1):
        new.append(None)
    dp.append(new)
dp[0][0] = tri[0][0]

for i in range(0, n-1):
    for j in range(0, i+1):
        for k in range(j, j+2):
            if dp[i+1][k] == None:
                dp[i+1][k] = dp[i][j] + tri[i+1][k]
            else:
                if dp[i][j] + tri[i+1][k] > dp[i+1][k]:
                    dp[i+1][k] = dp[i][j] + tri[i+1][k]            
print(max(dp[n-1]))

