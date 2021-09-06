def solve(n):
    if n % 2 != 0:
        return 0
    for i in range(2, n+1, 2):
        f[i] = f[i-2] + 2*g[i-1] 
        for j in range(i+1, n, 2):
            g[j] = f[j-1] + g[j-2]
    return f[n]

n = int(input())
f = [0 for _ in range(31)]
g = f[:]
f[0], g[1] = 1, 1
print(solve(n))

