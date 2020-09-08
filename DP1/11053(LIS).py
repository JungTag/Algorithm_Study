import sys
n = int(sys.stdin.readline().strip())
A = [int(x) for x in sys.stdin.readline().split()]
DP = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if A[i] > A[j]:
            DP[i] = max(DP[i], DP[j]+1)

print(max(DP))