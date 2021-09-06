import sys, collections

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

def bfs(cur, target):
    q = collections.deque([])
    q.append(cur+[0])
    visited[cur[0]][cur[1]] = 1

    while q:
        y, x, cnt = q.popleft()
        if y == target[0] and x == target[1]:
            print(cnt)
            break

        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny >= l or nx < 0 or nx >= l: # if 0 <= ny < l and 0 <= nx < l: 
                continue
            if not visited[ny][nx]:
                visited[ny][nx] = 1
                q.append([ny, nx, cnt + 1]) # visited에 cnt 넣어도 됨


n = int(sys.stdin.readline().strip())

for _ in range(n):
    l = int(sys.stdin.readline())
    visited = [[0 for _ in range(l)] for _ in range(l)]
    cur_pos = [int(x) for x in sys.stdin.readline().split()]
    target_pos = [int(x) for x in sys.stdin.readline().split()]

    bfs(cur_pos, target_pos)
