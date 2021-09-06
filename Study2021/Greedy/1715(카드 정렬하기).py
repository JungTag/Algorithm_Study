# https://www.acmicpc.net/problem/1715
import sys
import heapq as hq

def solve():
    result = 0
    for _ in range(n-1):
        min1 = hq.heappop(nums)
        min2 = hq.heappop(nums)
        sum_of_mins = min1 + min2
        result += sum_of_mins
        hq.heappush(nums, sum_of_mins)
    return result
        

# init
input = sys.stdin.readline
n = int(input().strip())
nums = [int(input().strip()) for _ in range(n)]
hq.heapify(nums)

print(solve())