import sys

def get_height():
    result = 0
    left, right = 0, MAX-1
    while left <= right:
        mid = (left+right) // 2
        _sum = get_sum(mid)
        if _sum < m:
            right = mid - 1
        elif _sum >= m:
            left = mid + 1
            result = mid
    return result

def get_sum(h):
    _sum = 0
    for tree in trees:
        diff = tree - h
        if diff > 0:
            _sum += diff
    return _sum

n, m = map(int, sys.stdin.readline().split())
trees = [int(x) for x in sys.stdin.readline().split()]

result = 0
MAX = max(trees)
print(get_height())
