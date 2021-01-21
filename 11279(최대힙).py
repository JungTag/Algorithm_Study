import sys
import heapq as hq

def get_max(x):
    if heap:
        _max = hq.heappop(heap)
        return _max[1]
    else:
        return 0

def insert_num(x):
    hq.heappush(heap, [-x, x])

n = int(sys.stdin.readline().strip())
heap = []

for _ in range(n):
    x = int(sys.stdin.readline().strip())
    if not x:
        print(get_max(x))
    else:
        insert_num(x)