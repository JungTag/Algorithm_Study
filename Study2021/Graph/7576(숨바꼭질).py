# https://www.acmicpc.net/problem/1697
import sys
import collections

def bfs():
    queue = collections.deque([[n, 0]])
    d = [-1, 1, 2]
    visited = set([n])
    while queue:
        cur, sec = queue.popleft()
        if cur == k:
            return sec
        for i in range(3):
            if i != 2:
                next = cur + d[i]
            else:
                next = cur * d[i]
            if 0 <= next <= 100000 and next not in visited:
                queue.append([next, sec+1])
                visited.add(next)

n, k = map(int, sys.stdin.readline().split())
print(bfs())