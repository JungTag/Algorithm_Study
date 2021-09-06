import sys
from bisect import bisect_left, bisect_right

def get_left_index():
    result = 0
    left, right = 0, n-1
    while left <= right:
        mid = (left+right) // 2
        if arr[mid] >= x:
            result = mid # 해당 인덱스에 위치!
            right = mid - 1
        else:
            left = mid + 1
    return result

def get_right_index():
    result = 0
    left, right = 0, n-1
    while left <= right:
        mid = (left+right) // 2
        if arr[mid] <= x:
            result = mid + 1 # 해당 인덱스보다 오른쪽에 위치!
            left = mid + 1
        else:
            right = mid - 1
    return result

n, x = map(int, sys.stdin.readline().split())
arr = [int(x) for x in sys.stdin.readline().split()]

result = get_right_index()-get_left_index()
if result == 0:
    print(-1)
else:
    print(result)

result2 = bisect_right(arr, x)-bisect_left(arr, x)
if result2 == 0:
    print(-1)
else:
    print(result2)