import sys
n = int(input())
P = [int(sys.stdin.readline().strip()) for i in range(n)]
for i in range(3):
    P.insert(0, 0)
DP = [0] * (n+3)

for i in range(3, n+3):
    DP[i] = max(DP[i-3] + P[i-1], DP[i-2]) + P[i]
print(DP[n+2])