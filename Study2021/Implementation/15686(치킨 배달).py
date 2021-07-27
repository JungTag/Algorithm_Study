# https://www.acmicpc.net/problem/15686
import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
g = []
houses = []
shops = []
for i in range(n):
    raw = []
    for j, x in enumerate(sys.stdin.readline().split()):
        if int(x) == 1:
            houses.append((i, j))
        elif int(x) == 2:
            shops.append((i, j))
        raw.append(int(x))
    g.append(raw)

result = []
for picked_shops in list(combinations(shops, m)):
    city_chicken_dist = 0 # 도시의 치킨 거리
    for hy, hx in houses:
        dists = []
        for sy, sx in picked_shops:
            dist = abs(hy-sy) + abs(hx-sx)
            dists.append(dist)
        city_chicken_dist += min(dists) # 각 집의 치킨거리를 더해줌
    result.append(city_chicken_dist)

print(min(result))

