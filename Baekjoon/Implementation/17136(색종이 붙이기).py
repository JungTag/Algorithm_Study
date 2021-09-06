import sys
sys.setrecursionlimit(10**9)

def dfs(cnt, papers, g):
    global result

    if cnt == REMAINS_LEN:
        if result != -1:
            result = min(result, sum(papers))
        else:
            result = sum(papers)
        return

    y, x = -1, -1
    for ry, rx in remains:
        if g[ry][rx]:
            y, x = ry, rx
            break

    max_size = expand(y, x, g)
    cos = []
    for size in range(1, max_size+1):
        if papers[size] + 1 > 5:
            continue
        for i in range(y, y+size):
            for j in range(x, x+size):
                g[i][j] = 0
                cos.append([i, j])
        papers[size] += 1
        dfs(cnt + size**2, papers, g)
        papers[size] -= 1
        for cy, cx in cos:
            g[cy][cx] = 1

def expand(y, x, g):
    for s in range(1, 6):
        for i in range(y, y+s):
            for j in range(x, x+s):
                if 0 <= i < 10 and 0 <= j < 10:
                    if g[i][j] == 0:
                        return s-1
                else:
                    return s-1
    return 5

org_g = [[int(x) for x in sys.stdin.readline().split()] for _ in range(10)]
remains = []
result = -1

for i in range(10):
    for j in range(10):
        if org_g[i][j]:
            remains.append([i, j])

REMAINS_LEN = len(remains)

dfs(0, [0 for _ in range(6)], org_g)
print(result)