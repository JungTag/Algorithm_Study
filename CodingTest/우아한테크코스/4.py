from collections import deque

def solution(n, board):
    answer = 0; visited = [False] * (n**2); visited_now = [[False] * (n) for _ in range(n)]
    dist = [[0] * (n) for _ in range(n)]
    Q = deque([[0,0]]); target = 1
    while Q:
        if False not in visited:
            break
        v = Q.popleft()
        raw, col = v[0], v[1]
        move = [[0, 1], [-1, 0], [0, -1], [1, 0]]
        # move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for i, j in move:
            current_raw, current_col = raw + i,  col + j
            if current_raw > n-1: current_raw = 0
            if current_raw < 0: current_raw = n-1
            if current_col > n-1: current_col = 0
            if current_col < 0: current_col = n - 1
            dist[current_raw][current_col] = dist[raw][col] + 1
            Q. append([current_raw, current_col])
            if target == board[current_raw][current_col]:
                visited[target-1] = True
                answer += (dist[current_raw][current_col]+1)
                dist = [[0] * (n) for _ in range(n)]
                target += 1
                Q = deque([[current_raw, current_col]])
                break        
    return answer

'''
문제점: 더 빠른 경로가 있음에도 불구하고 그걸 탐색하지 못함,
이유? 그냥 break로 종료시켜버리기 때문에!
'''

# def solution(n, board):
#     answer = 0; visited = [False] * (n**2)
#     dist = [[0] * (n) for _ in range(n)]
#     Q = deque([[0,0]]); target = 1
#     while Q:
#         if False not in visited:
#             break
#         v = Q.popleft()
#         raw, col = v[0], v[1]
#         move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
#         for i, j in move:
#             current_raw, current_col = raw + i,  col + j
#             if current_raw > n-1: current_raw = 0
#             if current_raw < 0: current_raw = n-1
#             if current_col > n-1: current_col = 0
#             if current_col < 0: current_col = n - 1
#             print(current_raw, current_col)
#             dist[current_raw][current_col] = dist[raw][col] + 1
#             Q. append([current_raw, current_col])
#             if target == board[current_raw][current_col]:
#                 visited[target-1] = True
#                 answer += (dist[current_raw][current_col]+1)
#                 dist = [[0] * (n) for _ in range(n)]
#                 target += 1
#                 Q = deque([[current_raw, current_col]])
#                 break        
#     return answer

n = 3; board = [[3, 5, 6], [9, 2, 7], [4, 1, 8]]
print(solution(n, board))