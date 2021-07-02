# https://www.acmicpc.net/problem/2170
import sys

n = int(sys.stdin.readline().strip())
points = [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)]
points.sort(key = lambda x: (x[0], x[1]))
start, end = points[0][0], points[0][1]
result = 0

for i in range(n-1):
    nx, ny = points[i+1]
    if end >= nx and ny > end:
        end = ny
    elif end < nx:
        result += end - start
        start, end = nx, ny
result += end - start

print(result)