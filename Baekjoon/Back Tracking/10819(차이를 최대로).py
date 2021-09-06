import sys, itertools

def cal_max(candi):
    result = 0
    for i in range(1, len(candi)):
        result += abs(candi[i-1] - candi[i])
    return result

n = int(sys.stdin.readline().strip())
arr = [int(x) for x in sys.stdin.readline().split()]
candis = list(itertools.permutations(arr, n))
MAX = float('-inf')

for candi in candis:
    num = cal_max(candi)
    if num > MAX:
        MAX = num

print(MAX)
            
