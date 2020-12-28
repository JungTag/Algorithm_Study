import sys
def combination(n, m):
    if n == m:
        return 1
    else:
        return factorial(m) // (factorial(m-n) * factorial(n))

def factorial(x):
    if x <= 1:
        return 1
    else:
        result = 1
        for i in range(2, x+1):
            result *= i
        return result

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    print(combination(n, m))
