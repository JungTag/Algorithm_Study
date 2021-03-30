import sys
sys.setrecursionlimit(10**9)

def dfs(depth, visited):
    global result

    if depth == limit:
        result = max(result, len(visited))
        return

    dfs(depth+1, visited) # 탐색 건너뜀

    idx = robots[depth]
    for i in range(idx-k, idx+k+1):
        if 0 <= i < n and i not in visited and line[i] == "H":
            visited.add(i)
            dfs(depth+1, visited)
            visited.remove(i)


n, k = map(int, sys.stdin.readline().split())
line = sys.stdin.readline().strip() # P는 로봇, H는 부품

result = limit = 0
robots = []
for i, x in enumerate(line):
    if x == "P":
        limit += 1
        robots.append(i)

dfs(0, set())
print(result)
