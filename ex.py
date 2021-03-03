...
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