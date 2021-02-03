import sys, collections

n = int(sys.stdin.readline().strip())

def bfs(start):
    q = collections.deque([])
    q.append(start)
    parent[start] = 1

    while q:
        cur = q.popleft()
        for adj in g[cur]:
            if not parent[adj]:
                parent[adj] = cur
                q.append(adj)  

g = collections.defaultdict(list)
parent = [0 for _ in range(n+1)]

for _ in range(n-1):
    u, v = map(int, sys.stdin.readline().split())
    g[u].append(v)
    g[v].append(u)

bfs(1)

for i in range(2, n+1):
    print(parent[i])