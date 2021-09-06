# https://www.acmicpc.net/problem/2170
'''
틀린 이유
1. min, max 함수 필요 X, 교체만 해주면 됨
2. 불필요한 값 할당 작업
'''
import sys

n = int(sys.stdin.readline().strip())
points = [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)]
points.sort(key = lambda x: (x[0], x[1]))
start, end = points[0][0], points[0][1]
result, temp = 0, end-start

for i in range(n-1):
    x1, y1 = points[i]
    x2, y2 = points[i+1]
    if y1 >= x2:
        start, end = min(start, x1), max(end, y1, y2)
    else:
        result += temp
        start, end = x2, y2
    temp = end-start

if temp != 0:
    result += temp

print(result)