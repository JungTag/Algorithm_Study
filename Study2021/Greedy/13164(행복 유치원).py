# https://www.acmicpc.net/problem/13164
import sys

def solve():
    diffs = []
    for i in range(n-1):
        diffs.append(heights[i+1] - heights[i])
    diffs.sort()
    if t > 1:
        diffs = diffs[:-(t-1)]
    return sum(diffs)

input = sys.stdin.readline
n, t = map(int, input().split())
heights = [int(x) for x in input().split()]

print(solve())