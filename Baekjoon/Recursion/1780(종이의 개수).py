import sys
sys.setrecursionlimit(10**9)

dy = [0, 0, 0, 1, 1, 1, 2, 2, 2]
dx = [0, 1, 2, 0, 1, 2, 0, 1, 2]

def dfs(y, x, k):
    _init = p[y][x]

    if k == 1:
        result[_init] += 1
        return

    for i in range(y, y+k):
        for j in range(x, x+k):
            if p[i][j] != _init:
                for i in range(9):
                    s = k//3
                    ny = y + s*dy[i]
                    nx = x + s*dx[i]
                    dfs(ny, nx, s)
                return
                    
    result[_init] += 1

n = int(sys.stdin.readline().strip())
p = []
result = {-1: 0, 0: 0, 1: 0}

for _ in range(n):
    _input = [int(x) for x in sys.stdin.readline().split()]
    p.append(_input)

dfs(0, 0, n)

for i in range(-1, 2):
    print(result[i])