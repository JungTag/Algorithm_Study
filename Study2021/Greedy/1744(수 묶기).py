# https://www.acmicpc.net/problem/1744
import sys
import heapq as hq

def solve():
    result = 0
    result += cal_heap(positive_nums, 1)
    result += cal_heap(negative_nums, 0)
    result += one_cnt
    return result

def cal_heap(nums, index):
    result = 0
    while nums:
        max1 = hq.heappop(nums)[index]
        if nums:
            max2 = hq.heappop(nums)[index]
            result += max1*max2
        else:
            if index == 0:
                if zero_cnt:
                    return result
            result += max1
    return result        


# init
input = sys.stdin.readline
n = int(input().strip())
positive_nums = []
negative_nums = []
zero_cnt = 0
one_cnt = 0
for _ in range(n):
    num = int(input().strip())
    if num > 1:
        positive_nums.append([-num, num])
    elif num < 0:
        negative_nums.append([num])
    elif num == 1:
        one_cnt += 1
    else:
        zero_cnt += 1
        
hq.heapify(positive_nums)
hq.heapify(negative_nums)

print(solve())