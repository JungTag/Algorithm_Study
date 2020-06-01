import math
A, B, V = map(int, input().split())
D = math.ceil((V-B)/(A-B))
print(D)
