# https://www.acmicpc.net/problem/12904
import sys

def solve():
    global t, s
    LEN_S = len(s)
    while len(t) >= LEN_S:
        if t == s:
            return 1
        if t[-1] == 'A':
            t = t[:-1]
        else:
            t = t[:-1][::-1]
    return 0

input = sys.stdin.readline
s = input().strip()
t = input().strip()

print(solve())