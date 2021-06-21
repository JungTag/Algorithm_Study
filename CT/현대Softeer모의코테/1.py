import sys

def get_sum():
    result = 0
    for i in range(n):
        result += (a[i] * p**(n-1-i)) % MOD
    return result % MOD

MOD = 1000000007
p, n = map(int, sys.stdin.readline().split())
a = [int(x) for x in sys.stdin.readline().split()]
    
print(get_sum())
