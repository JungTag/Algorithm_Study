# https://www.acmicpc.net/problem/11497
import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    ls = [int(x) for x in sys.stdin.readline().split()]
    ls.sort(reverse=True)
    result = 0
    for i in range(n-2):
        result = max(result, ls[i] - ls[i+2])
    print(result)