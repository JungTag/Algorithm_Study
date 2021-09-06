import sys
from itertools import combinations

n, s = map(int, sys.stdin.readline().split())
nums = [int(x) for x in sys.stdin.readline().split()]
# nums = list(set(nums)) -> 문제 이상함.. 중복 제거해줘야 하는데 중복 제거하면 틀린 거로 나옴

cnt = 0

# 콤비네이션을 이용한 풀이 -> 628ms
for i in range(1, n+1):
    combis = list(combinations(nums, i))
    for combi in combis:
        if sum(combi) == s:
            cnt += 1

print(cnt)

# 재귀를 이용한 풀이 -> 516ms
def solve(idx, total):
    global cnt
    if idx >= n:
        return   
    
    total += nums[idx]
    if total == s:
        cnt += 1

    solve(idx+1, total)
    solve(idx+1, total-nums[idx])

solve(0, 0)
print(cnt)