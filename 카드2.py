# https://www.acmicpc.net/problem/2164
import sys
from collections import deque


def solution(n):
    cards = deque([i for i in range(1, n+1)])
    left_cnt = n

    while left_cnt > 1:
        left_cnt -= 1
        cards.popleft()
        cards.append(cards.popleft())

    return cards[0]


input = sys.stdin.readline
n = int(input().strip())
print(solution(n))