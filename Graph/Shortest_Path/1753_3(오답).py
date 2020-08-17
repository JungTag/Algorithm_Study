import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
G = [[0]*(V+1) for _ in range(V+1)] # add dummy lines

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    G[u][v] = w

def Dijkstra(Graph):
    dist = [float('inf') for _ in range(V+1)]
    dist[1] = 0 # 시작 노드의 거리는 0으로 설정
    Q = []
    for v in range(V+1):
        Q.append((dist[v], v))
    heapq.heapify(Q)
    while Q:
        result = heapq.heappop(Q)
        u = result[1]
        for v in range(V+1):
            if G[u][v] != 0:
                if dist[v] > dist[u] + G[u][v]: # relax
                    old_dist = dist[v]
                    dist[v] = dist[u] + G[u][v]
                    Q.remove((old_dist, v))
                    Q.append((dist[v], v))
                    heapq.heapify(Q)
    for i in range(1, V+1):
        if dist[i] == float('inf'):
            print("INF")
        else:
            print(dist[i])

Dijkstra(G)