def binary_search(array, target, left, right):
    if left  > right:
        return None
    mid = (left + right) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, left, mid-1)
    else:
        return binary_search(array, target, mid+1, right)

def binary_search(array, target, left, right):
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return None    

from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

array = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 원소의 개수 출력
print(count_by_range(array, 4, 4)) # 2

# 값이 [-1, 3] 범위에 있는 원소의 개수 출력
print(count_by_range(array, -1, 3)) # 6

