import sys

p = [0 for _ in range(101)]
p[:5] = [1, 1, 1, 2, 2]

for i in range(5, 100):
    p[i] = p[i-1] + p[i-5]

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    print(p[n-1])