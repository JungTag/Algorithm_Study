import sys

def flatten(h):
    time = 0
    for i in range(n):
        for j in range(m):
            if g[i][j] == h:
                continue
            elif g[i][j] > h:
                time += (2 * (g[i][j] - h))
            else:
                time += (h- g[i][j])
    return [time, h]

n, m, b = map(int, sys.stdin.readline().split())
g = [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)]
result = [float('inf'), 0]
_sum = b

for i in range(n):
    for j in range(m):
        _sum += g[i][j]

_max = min(257, _sum//(n*m) + 1)

for h in range(0, _max):
    time, height = flatten(h)
    if time <= result[0]:
        result[0] = time
        if height > result[1]:
            result[1] = height

print(*result)
