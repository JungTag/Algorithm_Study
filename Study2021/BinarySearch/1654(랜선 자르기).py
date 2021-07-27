# https://www.acmicpc.net/problem/1654
# left = 0, result = 0 했더니 틀림, 초기값 설정 중요!
import sys

def search():
    result = 1
    left, right = 1, cables[-1]
    while left <= right:
        mid = (left+right) // 2
        if is_possible(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result

def is_possible(criteria):
    cnt = 0
    for cable in cables:
        cnt += (cable // criteria)
    if cnt >= n:
        return True
    else:
        return False

k, n = map(int, sys.stdin.readline().split())
cables = [int(sys.stdin.readline().strip()) for _ in range(k)]
cables.sort()
print(search())