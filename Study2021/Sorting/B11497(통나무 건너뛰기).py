# https://www.acmicpc.net/problem/11497
'''
이상하게 품... 리스트 생성하는데 시간 오래 걸림..
'''
import sys

def centralize():
    new_ls = []
    for i, l in enumerate(ls):
        if i % 2 == 0:
            new_ls = [l] + new_ls
        else:
            new_ls = new_ls + [l]
    return new_ls

def cal_gap():
    max_gap = float('-inf')
    new_ls = [ls[-1]] + ls
    for i in range(1, n+1):
        gap = abs(new_ls[i]-new_ls[i-1])
        if gap > max_gap:
            max_gap = gap
    return max_gap

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    ls = [int(x) for x in sys.stdin.readline().split()]
    ls.sort(reverse=True)
    ls = centralize()
    print(cal_gap())