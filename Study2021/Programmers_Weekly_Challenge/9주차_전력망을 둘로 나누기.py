# https://programmers.co.kr/learn/courses/30/lessons/86971?language=python3
import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

def solution(n, wires):
    answer = float('inf')

    def dfs(cur, cnt):
        visited[cur] = 1
        cnt += 1
        for adj in g[cur]:
            if not visited[adj]:
                cnt = dfs(adj, cnt)
        return cnt   

    # init graph
    for i in range(n-1):
        g = defaultdict(list)

        for idx, wire in enumerate(wires):
            if idx == i:
                continue
            g[wire[0]].append(wire[1])
            g[wire[1]].append(wire[0])

        # travel graph
        visited = [0 for _ in range(n+1)]
        area = []

        for node in range(1, n+1):
            if not visited[node]:
                area.append(dfs(node, 0))

        answer = min(answer, abs(area[0] - area[1]))

    return answer

print(solution(	9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))


'''
그래프의 엣지를 하나씩 지워보고 브루트포스..?
트리 형태 -> node: n일 때 edeg: n- 1

for문 돌면서 엣지 하나씩 제외시켜서 그래프를 초기화한다.
그 다음 거기서 다시 for문 돌면서 쌍 몇개씩 나오는지 체크
- 간선을 하나 없애면 무조건 2분할됨(트리의 특성)
'''