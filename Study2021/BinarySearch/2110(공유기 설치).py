# https://www.acmicpc.net/problem/2110
import sys

def search():
    result = 0
    left, right = 1, cos[-1]-cos[0]
    while left <= right:
        mid = (left+right) // 2
        if is_possible(mid, c-1):
            result = mid
            left = mid+1
        else:
            right = mid-1
    return result

def is_possible(diff, cnt):
    nearest = 0
    for i in range(1, n):
        if cos[i]-cos[nearest] >= diff:
            cnt -= 1
            nearest = i
        if cnt <= 0:
            break
    if cnt > 0:
        return False
    else:
        return True

n, c = map(int, sys.stdin.readline().split())
cos = [int(sys.stdin.readline().strip()) for _ in range(n)]
cos.sort()
print(search())
