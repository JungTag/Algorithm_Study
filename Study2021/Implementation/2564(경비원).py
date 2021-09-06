# https://www.acmicpc.net/problem/2564
import sys

def solve():
    result = 0
    t_dir, t_dist = target
    for dir, dist in shops:
        if t_dir == 1:
            if dir == 1:
                result += abs(t_dist - dist)
            elif dir == 2:
                result += h + min(dist + t_dist, (w - t_dist) + (w - dist))
            elif dir == 3:
                result += t_dist + dist
            else:
                result += (w - t_dist) + dist
        elif t_dir == 2:
            if dir == 1:
                result += h + min(dist + t_dist, (w - t_dist) + (w - dist))
            elif dir == 2:
                result += abs(t_dist - dist)
            elif dir == 3:
                result += t_dist + (h - dist)
            else:
                result += (w - t_dist) + (h - dist)
        elif t_dir == 3:
            if dir == 1:
                result += t_dist + dist
            elif dir == 2:
                result += (h - t_dist) + dist
            elif dir == 3:
                result += abs(t_dist - dist)
            else:
                result += w + min(dist + t_dist, (h - t_dist) + (h - dist))
        else:
            if dir == 1:
                result += (w - dist) + t_dist
            elif dir == 2:
                result += (h - t_dist) + (w - dist)
            elif dir == 3:
                result += w + min(dist + t_dist, (h - t_dist) + (h - dist))
            else:
                result += abs(t_dist - dist)
    return result

input = sys.stdin.readline

w, h = map(int, input().split())
n = int(input().strip())
shops = [[int(x) for x in input().split()] for _ in range(n)]
target = [int(x) for x in input().split()]

print(solve())