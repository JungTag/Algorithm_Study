import sys, collections
# sys.setrecursionlimit(10**6)

n, m, v = map(int, sys.stdin.readline().split())
g = collections.defaultdict(list)

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())

    if x not in g[y] and y not in g[x]:
        g[x].append(y)
        g[y].append(x)
        g[x].sort()
        g[y].sort()

def DFS(cur, visited):
    visited.append(cur)

    for u in g[cur]:
        if u not in visited:
            DFS(u, visited)

    return visited
    
def BFS():
    global q
    global visited

    while q:
        cur = q.popleft()
        
        for u in g[cur]:
            if u not in visited:
                visited.append(u)
                q.append(u)
    
    print(*visited)

print(*DFS(v, []))
q = collections.deque([v])
visited = [v]
BFS()