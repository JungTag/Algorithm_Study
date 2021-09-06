import sys, collections
sys.setrecursionlimit(10**6)

def make_graph(n, p):
    g = collections.defaultdict(int)
    for i in range(1, n+1):
        g[i] = p[i-1]
    return g        

def dfs(u):
    global g
    global visited

    visited[u] = 1

    if not visited[g[u]]:
        dfs(g[u])

t = int(sys.stdin.readline().strip())

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    p = [int(x) for x in sys.stdin.readline().split()]
    cnt = 0

    g = make_graph(n, p)
    visited = [0 for _ in range(n+1)]

    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)
            cnt += 1
    
    print(cnt)
