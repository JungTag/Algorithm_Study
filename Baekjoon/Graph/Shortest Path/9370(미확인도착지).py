import sys
import heapq

'''
문제를 푸는 아이디어는 기본적으로 2가지가 존재했다.

1. g->h 경로를 지났을 때 check!
=> 방법이 잘 안 떠올랐다.

2. 다익스트라를 2번 돌림
- 출발 노드로부터 전체 노드의 최단경로를 찾고 중간 지점을 반환
- 중간 지점에서 목적지 노드까지의 거리를 계산
이때, 출발지에서 더 가까운 노드를 g, 더 먼 노드를 h라 한다.
즉, 모든 목적지 노드에 대해서
출발지 ~ 목적지 == 출발지 ~ 중간지점(h) + 중간지점(h) ~ 목적지가 성립하는지 비교한다.

# 발생했던 문제점
- 끊겨 있는 노드에 대해서 예외 처리를 해주지 않았다.
- 목적지가 중간지점에 껴있는 경우에 대해 처리를 해주지 않았다.
 - 이때, 목적지가 g라면 g->h를 지나지 못하므로 목적지 리스트에서 제거한다. 

# 출력시
출력시 for문을 돌려서 print(elem, end = " ")하는 것보다
그냥 print(*list)하는 게 훨씬 편하다!
'''
def get_middle_point(Graph):
    Q = [] # Q <- (distance, vertex)
    Q.append([dist[s], s])
    while Q:
        u = heapq.heappop(Q)[1]
        for v, c in G[u]: # edge = (vertex, cost)
            if dist[v] > dist[u] + c:
                dist[v] = dist[u] + c
                heapq.heappush(Q, [dist[v], v])
    if dist[g] < dist[h]:
        if g in goal_list:
            goal_list.remove(g)
        return h
    else:
        if h in goal_list:
            goal_list.remove(h)
        return g

def calc_distance_middle_to_goal(Graph, goal_list):
    Q = [] # Q <- (distance, vertex)
    Q.append([middle_dist[middle_point], middle_point])
    while Q:
        u = heapq.heappop(Q)[1]
        for v, c in G[u]: # edge = (vertex, cost)
                if middle_dist[v] > middle_dist[u] + c:
                    middle_dist[v] = middle_dist[u] + c
                    heapq.heappush(Q, [middle_dist[v], v])
    

T = int(sys.stdin.readline().strip())
INF = float('inf')

for _ in range(T):
    n, m, t = map(int, sys.stdin.readline().split())
    s, g, h = map(int, sys.stdin.readline().split())
    G = {i:[] for i in range(1, n+1)}
    goal_list = []

    for _ in range(m):
        a, b, d = map(int, sys.stdin.readline().split())
        G[a].append([b, d])
        G[b].append([a, d])
    
    for _ in range(t):
        goal_list.append(int(sys.stdin.readline().strip()))

    dist = [INF] * (n+1)   
    dist[s] = 0

    middle_point = get_middle_point(G) #
    middle_dist = [INF] * (n+1)
    middle_dist[middle_point] = 0

    calc_distance_middle_to_goal(G, goal_list) #

    result = []
    for goal in goal_list:
        if dist[goal] != INF and dist[goal] == dist[middle_point] + middle_dist[goal]:
            result.append(goal)
    result.sort()
    print(*result)