import sys, collections

def bfs(start, end):
    q = collections.deque([])
    q.append([start,0])
    visited[start] = 1

    while q:
        cur, cnt = q.popleft()
        if cur == end:
            print(cnt)
            return
        for adj in g[cur]:
            if not visited[adj]:
                visited[adj] = 1
                q.append([adj,cnt+1])

    print(-1)

n = int(sys.stdin.readline().strip())
t1, t2 = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline().strip())

g = collections.defaultdict(list)
visited = [0 for _ in range(n+1)]

for _ in range(m):
    y, x = map(int, sys.stdin.readline().split())
    g[y].append(x)
    g[x].append(y)

bfs(t1, t2)