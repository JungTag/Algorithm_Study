import sys
sys.setrecursionlimit(10**9)

n = int(input())
w = []
INF = float('inf')
dp = [[INF for _ in range(n)] for i in range(2**n)]

for _ in range(n):
    raw = [int(x) for x in sys.stdin.readline().split()]
    w.append(raw)

def travel(visited, cur):
    visited = visited | (1 << cur) # 방문한 도시를 기록

    if visited == (1 << n) - 1: # 모든 도시를 방문한 경우
        if w[cur][0] != 0: # 출발 도시로 갈 수 있는 경로가 있는 경우 
            return w[cur][0]
        else:
            return INF
    
    if dp[visited][cur] != INF: # dp[현재까지 방문한 도시들][현재 도시] -> 현재 도시에서 출발 도시까지 돌아가는 데 필요한 비용 
        return dp[visited][cur]
    
    for u in range(n):
        if u != cur and (visited & (1 << u)) == 0 and w[cur][u] != 0: # 1) 현재 도시가 아니고 2) 아직 방문하지 않았으며 3) 경로가 있는 도시를 찾는다.
            cost = travel(visited, u) + w[cur][u]
            if dp[visited][cur] > cost:
                dp[visited][cur] = cost

    return dp[visited][cur]

print(travel(0, 0)) # 사이클 때문에 어느 도시에서 출발하든 최소 비용은 같다. 따라서 출발 도시는 0번 도시로 한다. 
    



