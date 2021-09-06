import sys, itertools, copy

def rotate(pm, arr):
    result = float('inf')
    while pm:
        r, c, s = pm.pop()
        uy, ux, ly, lx = r-s, c-s, r+s, c+s
        while uy < ly and ux < lx:
            t1, t2, t3 = arr[uy][lx], arr[ly][lx], arr[ly][ux]
            for x in range(lx, ux, -1):
                arr[uy][x] = arr[uy][x-1]
            for y in range(ly, uy, -1):
                arr[y][lx] = arr[y-1][lx]
            arr[uy+1][lx] = t1 
            for x in range(ux, lx):
                arr[ly][x] = arr[ly][x+1]
            arr[ly][lx-1] = t2
            for y in range(uy, ly):
                arr[y][ux] = arr[y+1][ux]
            arr[ly-1][ux] = t3
            uy, ux, ly, lx = uy+1, ux+1, ly-1, lx-1
    for i in range(1, n+1):
        raw_sum = sum(arr[i])
        result = min(result, raw_sum)
    return result

arr, ops = [], []
n, m, k = map(int, sys.stdin.readline().split())
org_arr = [[0 for _ in range(m+1)]]+[[0]+[int(x) for x in sys.stdin.readline().split()] for _ in range(n)]
ops = [[int(x) for x in sys.stdin.readline().split()] for _ in range(k)]
min_value = float('inf')

for pm in list(itertools.permutations(ops, k)):
    result = rotate(list(pm), copy.deepcopy(org_arr))
    min_value = min(min_value, result)

print(min_value)