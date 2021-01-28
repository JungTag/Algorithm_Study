import sys

def get_prime(m, n):
    for i in range(2, n+1):
        if isPrime[i]:
            for j in range(2*i, n+1, i):
                isPrime[j] = False
    for i in range(m, n+1):
        if isPrime[i]:
            print(i)

m, n = map(int, sys.stdin.readline().split())
isPrime = [False]*2 + [True for _ in range(n-1)]

get_prime(m, n)