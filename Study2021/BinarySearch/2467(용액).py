# https://www.acmicpc.net/problem/2467
import sys

def search():
    left, right = 0, n-1
    while left < right:
        mid = values[left] + values[right]
        if abs(mid) < abs(result[0]):
            result[0], result[1], result[2] = mid, values[left], values[right]
        if mid > 0:
            right -= 1
        elif mid < 0:
            left += 1
        else:
            return 

n = int(sys.stdin.readline().strip())
values = [int(x) for x in sys.stdin.readline().split()]
values.sort()
result = [float('-inf'), values[0], values[-1]] # [sum, v1, v2]
search()
print(result[1], result[2])