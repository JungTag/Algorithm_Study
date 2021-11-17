from collections import deque

def solution(macaron):
    answer = []
    GRAPH_SIZE = 6
    DELETE_CNT = 3

    g = [[0 for _ in range(GRAPH_SIZE)] for _ in range(GRAPH_SIZE)]

    macaron_cnt = 0

    # insert macaron
    for col, color in macaron:
        col -= 1
        drop_row = GRAPH_SIZE - 1

        for row in range(GRAPH_SIZE):
            if g[row][col]:
                drop_row = row - 1
                break
        
        if drop_row == -1:
            continue
    
        g[drop_row][col] = color
        macaron_cnt += 1

        if macaron_cnt < DELETE_CNT:
            continue

        # graph traversal
        cnt, deleted = bfs(g, [drop_row, col, color], GRAPH_SIZE)

        # delete & drop macaron
        for row in range(GRAPH_SIZE):
            for col in range(GRAPH_SIZE):
                if [row, col] in deleted:
                    next_row = row+1
                    if next_row < GRAPH_SIZE:
                        g[row][col] = g[next_row][col]
                        g[next_row][col] = 0
                    else:
                        g[row][col] = 0
                    macaron_cnt -= 1

    print(g)

    return answer

def bfs(g, start, GRAPH_SIZE):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    visited = [[0 for _ in range(GRAPH_SIZE)] for _ in range(GRAPH_SIZE)]
    queue = deque([start])
    deleted = []
    cnt = 0

    while queue:
        y, x, color = queue.popleft()
        deleted.append([y, x])
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < GRAPH_SIZE and 0 <= nx < GRAPH_SIZE:
                if not visited[ny][nx] and g[ny][nx] == color:
                    visited[ny][nx] = 1
                    queue.append([ny, nx, color])
                    cnt += 1    

    return cnt, deleted
                    
print(solution(	[[1, 1], [2, 1], [1, 2], [3, 3], [6, 4], [3, 1], [3, 3], [3, 3], [3, 4], [2, 1]]))