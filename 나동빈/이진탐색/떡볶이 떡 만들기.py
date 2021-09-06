import sys

def cal_sum(criteria):
    result = 0
    for length in lengths:
        if length > criteria:
            result += (length - criteria)
    return result
    
def binary_search():
    result = 0
    left, right = 0, max(lengths)
    while left <= right:
        mid = (left+right) // 2
        if cal_sum(mid) >= m:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result

n, m = map(int, sys.stdin.readline().split())
lengths = [int(x) for x in sys.stdin.readline().split()]
print(binary_search())

