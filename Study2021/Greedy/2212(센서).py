# https://www.acmicpc.net/problem/2212
import sys

def solve():
    diffs = []
    for i in range(n-1):
        diffs.append(censors[i+1] - censors[i])
    diffs.sort()
    if k > 1:
        diffs = diffs[:-(k-1)]
    return sum(diffs)

input = sys.stdin.readline
n = int(input().strip())
k = int(input().strip())
censors = sorted([int(x) for x in input().split()])

print(solve())