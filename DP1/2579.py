import sys
n = int(input())
P = [int(sys.stdin.readline().strip()) for i in range(n)]
P.insert(0, 0)
DP = [0] * (n+1)
DP2 = [0] * (n+1)
def solve(n):
    if n == 1:
        DP[1] = P[1]
        return DP[1]
    DP[1], DP[2] = P[1], P[2]
    DP2[1], DP2[2] = P[1], P[1] + P[2]
    if n == 2:
        return DP[1] + DP[2]
    if n == 3:
        return max(DP[1]+P[3], DP[2]+P[3])    
    for i in range(4, n+1):
        if DP[i-1] != DP[i-2] + P[i-1]:
            DP[i] = max(DP[i-1], DP[i-2]) + P[i]
        else:
            if i != n:
                DP[i+1] = DP[i-1] + P[i+1]
            else:
                DP[i] = DP[i-2] + P[i]
    for i in range(4, n+1):
        if DP2[i-1] != DP2[i-2] + P[i-1]:
            DP2[i] = max(DP2[i-1], DP2[i-2]) + P[i]
        else:
            if i != n:
                DP2[i+1] = DP2[i-1] + P[i+1]
            else:
                DP2[i] = DP2[i-2] + P[i]
    return max(DP[n], DP2[n])

print(solve(n))