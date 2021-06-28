# https://www.acmicpc.net/problem/1946
import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    workers = [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)]
    workers.sort()
    min_score = workers[0][1]
    cnt = 1
    for i in range(n):
        score = workers[i][1]
        if score < min_score:
            min_score = score
            cnt += 1
    print(cnt)