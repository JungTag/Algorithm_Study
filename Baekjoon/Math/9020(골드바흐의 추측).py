import sys

def get_prime(MAX):
    for i in range(2, MAX+1):
        if isPrime[i]:
            for j in range(2*i, MAX+1, i):
                isPrime[j] = False

def get_goldbach_partition(n):
    l = r = n//2
    while True:
        while not isPrime[l]:
            l -= 1
        while not isPrime[r]:
            r += 1
        if l + r == n:
            return [l, r]
        elif l + r > n:
            l -= 1
        else:
            r += 1

MAX = 10000
t = int(sys.stdin.readline().strip())
isPrime = [False]*2 + [True for _ in range(MAX-1)]

get_prime(MAX)

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    print(*get_goldbach_partition(n))