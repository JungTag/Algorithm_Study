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

'''
코드는 이게 더 깔끔, 속도는 위 코드가 더 빠름
카드 i를 구하는 최대 비용 => 아래 식 중에서 최대
p[1] + dp[i-1]
p[2] + dp[i-2]
~
p[i] + dp[0]
즉, dp[i] = p[k] + dp[i-k]
이를 표현하면 dp[i] = max(dp[i], p[k] + dp[i-k])


N = int(input())
p = [0] + list(map(int,input().split()))
dp = [0 for _ in range(N+1)]


for i in range(1,N+1):
    for k in range(1,i+1):
        dp[i] = max(dp[i], dp[i-k] + p[k])
print(dp[i])
'''
