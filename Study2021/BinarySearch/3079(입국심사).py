# https://www.acmicpc.net/problem/3079
import sys

def search():
    left, right = 1, 10**18
    result = right
    while left <= right:
        mid = (left+right) // 2
        if is_possible(mid):
            result = mid
            right = mid-1
        else:
            left = mid+1
    return result

def is_possible(target):
    result = 0
    for time in times:
        result += target//time
        if result >= t:
            return True
    return False

n, t = map(int, sys.stdin.readline().split())
times = [int(sys.stdin.readline().strip()) for _ in range(n)]
times.sort()

print(search())