from collections import deque

def solution(cakes, cut_rows, cut_columns):
    answer = 0
    max_row = len(cakes)
    max_column = len(cakes[0])

    visited = [[0 for _ in range(max_column)] for _ in range(max_row)]

    cut_rows.append(max_row)
    cut_columns.append(max_column)
    
    cur_row = 0
    cur_column = 0
    start_points = []

    for cut_row in cut_rows:
        for cut_column in cut_columns:
            start_points.append([cur_row, cur_column, cut_row-1, cut_column-1])
            cur_column = cut_column
        cur_column = 0
        cur_row = cut_row

    for s_row, s_col, e_row, e_col in start_points:
        answer = max(answer, bfs(s_row, s_col, e_row, e_col, visited, cakes))

    return answer

def bfs(s_row, s_col, e_row, e_col, visited, cakes):
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    visited[s_row][s_col] = 1
    queue = deque([[s_row, s_col]])
    kinds = set([cakes[s_row][s_col]])
    
    while queue:
        y, x= queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if s_row <= ny <= e_row and s_col <= nx <= e_col:
                if not visited[ny][nx]:
                    visited[ny][nx] = 1
                    queue.append([ny, nx])
                    kinds.add(cakes[ny][nx])

    return len(kinds)

print(solution(["AAAACX", "AAAACX", "AAAACX", "ZZZZZX", "ATTTTX", "XUUUUU"], [1,2,4], [2,3]))