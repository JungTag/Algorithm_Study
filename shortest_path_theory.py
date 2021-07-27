import collections, heapq
graph = collections.defaultdict(list)

for u, v, w in inputs: # 양방향 그래프라고 가정
    graph[u].append([v, w])
    graph[v].append([u, w])

def Dijkstra(start):
    dist = [float('inf')] * (V+1) # V는 노드의 개수
    dist[start] = 0 # 시작 노드의 거리는 0으로 설정
    Q = []
    Q.append([dist[start], start]) 
    while Q:
        u = heapq.heappop(Q)[1]
        for v, w in G[u]: # edge = (vertex, weight)
            if dist[v] > dist[u] + w: 
                dist[v] = dist[u] + w
                heapq.heappush(Q,[dist[v], v])
    return dist


for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    g[a].append([b, c])

def bellman_ford(s):
    dist = [INF] * (V+1) # V는 노드의 개수
    dist[s] = 0 # 시작 노드의 거리는 0으로 설정
    for _ in range(V-1):
        for u in range(1, V+1):
            for v, c in graph[u]:
                if dist[v] > dist[u] + c:
                    dist[v] = dist[u] + c
    for u in range(1, V+1): # 음수 사이클이 존재하는지 체크
        for v, c in graph[u]:
            if dist[v] > dist[u] + c:
                return False
    return dist