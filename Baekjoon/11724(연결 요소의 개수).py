import sys, collections

G = collections.defaultdict(list)
visited = {}

N, M = map(int, sys.stdin.readline().split())
for _ in range(M):
    u, v = sys.stdin.readline().split()
    G[u].append(v)
    G[v].append(u)
    visited[u] = False
    visited[v] = False

stack = []
cnt = 0
node_list = list(visited.keys())

diff = N-len(node_list)
if diff != 0:
    cnt += diff

while node_list:
    cnt += 1
    stack.append(node_list[-1])
    while stack:
        node = stack.pop()
        for v in G[node]:
            if visited[v] == False:
                stack.append(v)
                visited[v] = True
                node_list.remove(v)
                    
print(cnt)

'''
더 나은 풀이
import sys
sys.setrecursionlimit(10000)

def dfs(v):
    visited[v] = True
    for e in adj[v]:
        if not visited[e]:
            dfs(e)
            
N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
count = 0

for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
    
for j in range(1, N + 1):
    if not visited[j]:
        dfs(j)
        count += 1

print(count)
'''