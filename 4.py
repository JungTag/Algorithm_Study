import sys, math

t = int(input())

for _ in range(t):
    x, y = map(int, sys.stdin.readline().split())
    dist = y - x

    std = math.ceil(math.sqrt(dist))

    left = (std-1) ** 2
    right = std ** 2
    mid = (left + right) / 2

    if dist >= mid:
        print(std * 2 - 1)
    else:
        print(std * 2 - 2)
