# https://www.acmicpc.net/problem/3020
import sys
from bisect import bisect_left

def search():
    min_value = float('inf')
    cnt = 1

    for h in range(1, t+1):
        top_idx, bot_idx = bisect_left(tops, (t+1)-h), bisect_left(bottoms, h)
        obs_cnt = n - (top_idx+bot_idx)
        if obs_cnt < min_value:
            min_value = obs_cnt
            cnt = 1
        elif obs_cnt == min_value:
            cnt += 1
    return min_value, cnt


n, t = map(int, sys.stdin.readline().split())
tops, bottoms = [], []

for i in range(n):
    height = int(sys.stdin.readline().strip())
    if i % 2 == 0:
        bottoms.append(height)
    else:
        tops.append(height)

tops.sort()
bottoms.sort()

print(*search())