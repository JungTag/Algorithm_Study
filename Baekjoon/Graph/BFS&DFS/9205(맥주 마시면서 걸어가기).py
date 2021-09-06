import sys, collections

def check():
    q = collections.deque([start])
    visited = set()
    while q:
        x, y = q.popleft()
        if abs(x-dst[0]) + abs(y-dst[1]) <= 1000:
            return True
        for i in range(n):
            if i not in visited:
                nx, ny = cos[i]
                if abs(x-nx) + abs(y-ny) <= 1000:
                    q.append([nx, ny])
                    visited.add(i)
    return False
        
t = int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    start = [int(x) for x in sys.stdin.readline().split()]
    cos = [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)]
    dst = [int(x) for x in sys.stdin.readline().split()]
    if check():
        print("happy")
    else:
        print("sad")