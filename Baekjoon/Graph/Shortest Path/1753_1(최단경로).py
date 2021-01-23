import sys
import heapq

'''
발생했던 문제점
1) 사용한 자료구조의 문제
1. 인접행렬로 풀음 -> 메모리가 너무 커짐(인접행렬의 공간복잡도는 O(V^2), V가 최대 20000개까지 주어진다는 점을 고려할 때 문제가 발생함)
2. 인접리스트를 클래스로 구현해서 풀음 -> 한방향연결리스트의 특성상 Search연산에서 너무 많은 시간을 잡아먹는다. 다시 말해 인접을 확인할 때 시간이 너무 오래 걸림
3. 이중 딕셔너리로 풀음 -> 중복간선이 해결되지 않는다. 왜냐하면 딕셔너리의 특성상 중복키를 허용하지 않기 때문이다.

2) 풀이의 문제
일단 기본적으로 신찬수 교수님의 강의와 예전에 과제로 구현해둔 다익스트라 알고리즘을 참고했다.
여기서 문제가 발생했다.
1. 굳이 Q에 모든 pair(dist[vertex], vertex)를 채워넣을 필요가 없었다.
- relax가 발생할 때만 큐에 삽입을 해주면 된다.
- 또 모든 pair를 삽입하게 되면 relax가 일어날 때 필요없는 연산이 발생한다.
- 게다가 heapify연산도 계속 해줘야 한다.
2. relax가 일어날 때 중복되는 pair(ex: (4,2) (3,2))를 고려할 필요가 없었다.
why?
- 우선순위큐(min-heap)를 사용하기 때문에 dist[vertex]가 적은 데이터부터 pop된다.
- 이 과정에서 해당 정점과 인접한 정점들의 거리가 갱신되므로, 그 후에 pop되는 중복 pair에선 relax가 일어나지 않는다.
3. 시작점이 무조건 1이 아님에도 불구하고 1로 시작한다고 가정했다.
- 문제의 조건을 잘 읽지 않아서 발생한 문제이다.

=> 이차원 리스트에서 for x,y in my_list 이런 식으로 pair추출이 가능한 점을 항상 명심해두자!
'''
V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
G = {i:[] for i in range(1, V+1)}

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    G[u].append([v,w])

def Dijkstra(Graph):
    dist = [float('inf')] * (V+1)
    dist[K] = 0 # 시작 노드의 거리는 0으로 설정
    Q = [] # Q -> (weight, vertex)
    Q.append([dist[K], K]) 
    while Q:
        u = heapq.heappop(Q)[1]
        for v, w in G[u]: # edge = (vertex, weight)
            if dist[v] > dist[u] + w: # relax
                dist[v] = dist[u] + w
                heapq.heappush(Q,[dist[v], v])
    for i in range(1, V+1):
        if dist[i] == float('inf'):
            print("INF")
        else:
            print(dist[i])

Dijkstra(G)
