import sys, collections

n = int(sys.stdin.readline().strip())
a = [int(x) for x in sys.stdin.readline().split()]
m = int(sys.stdin.readline().strip())
nums = [int(x) for x in sys.stdin.readline().split()]

a = set(a)
result = collections.defaultdict(int)

for i in range(m):
    if nums[i] in a:
        result[i] = 1
    else:
        result[i] = 0

for i in range(m):
    print(result[i])