# https://www.acmicpc.net/problem/1138
import sys


def solution(n, people):
    INF = float('inf')
    line = [INF for _ in range(n)]

    for i in range(n):
        height1 = i+1
        higher_cnt = people[i]
        cnt = 0

        for j, height2 in enumerate(line):
            if cnt == higher_cnt:
                if line[j] == INF:
                    line[j] = height1
                else:
                    continue
            if height2 > height1:
                cnt += 1
                
    return line


input = sys.stdin.readline
n = int(input().strip())
people = [int(x) for x in input().split()]

print(*solution(n, people))