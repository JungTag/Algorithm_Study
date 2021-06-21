from collections import deque

def solution(n, horizontal):
    # visit = [[False] * (m+2) for _ in range(n+2)]
    answer = [[0] * n for _ in range(n)]
    right = horizontal  # 방향 설정
    curr_sec = 0
    Q = deque([])
    dir = [[1,0], [1,-1], [-1,1], [0,1]] # 하, 좌-하, 우-상, 우
    if horizontal == True:
        answer[0][1] = 1
        Q.append([0, 1, dir[3]]) # 다음 갈 좌표 + 어떤 방향에서 왔는가?
    else:
        answer[1][0] = 1
        Q.append([1, 0, dir[0]]) 
    while Q:
        v = Q.popleft()
        raw, col, curr_dir = v[0], v[1], v[2]
        i, j = curr_dir
        if raw == 0 or raw == n-1:
            if curr_dir == dir[1]: # 좌-하에서 왔다면(raw == n-1)
                k, l = dir[3] # 우로 간다
                answer[raw][col] = answer[raw-i][col-j] + 2
                Q.append([raw+k, col+l, dir[3]])
            if curr_dir == dir[2]: # 우-상에서 왔다면
                k, l = dir[3] # 우로 간다
                answer[raw][col] = answer[raw-i][col-j] + 2
                Q.append([raw+k, col+l, dir[3]])
            if curr_dir == dir[3]: # 우에서 왔다면(raw == 0 or raw == n-1)
                if raw == 0:
                    k, l = dir[1] # 좌-하로 간다
                    answer[raw][col] = answer[raw-i][col-j] + 1
                    Q.append([raw+k, col+l, dir[1]])                    
                else: 
                    k, l = dir[2] # 우-상으로 간다
                    answer[raw][col] = answer[raw-i][col-j] + 1
                    Q.append([raw+k, col+l, dir[2]])
            if raw == n-1 and col == n-1:
                if curr_dir == dir[0]:
                    answer[raw][col] = answer[raw-i][col-j] + 1
        elif col == 0 or col == n-1: 
            if curr_dir == dir[1] or curr_dir == dir[2]: # 좌-하 or 우-상에서 왔다면
                k, l = dir[0] # 하로 간다
                answer[raw][col] = answer[raw-i][col-j] + 2
                Q.append([raw+k, col+l, dir[0]])
            if curr_dir == dir[0]: # 하에서 왔다면
                if col == 0:
                    k, l = dir[2] # 우-상으로 간다
                    answer[raw][col] = answer[raw-i][col-j] + 1
                    Q.append([raw+k, col+l, dir[2]])
                else:
                    k, l = dir[1] # 좌-하으로 간다
                    answer[raw][col] = answer[raw-i][col-j] + 1
                    Q.append([raw+k, col+l, dir[1]])                        
        else: # 중간에 있는 애들
            if curr_dir == dir[1]:
                k, l = dir[1] 
                answer[raw][col] = answer[raw-i][col-j] + 2
                Q.append([raw+k, col+l, dir[1]])
            if curr_dir == dir[2]:
                k, l = dir[2]
                answer[raw][col] = answer[raw-i][col-j] + 2
                Q.append([raw+k, col+l, dir[2]])
        if answer[n-1][n-1] != 0:
            break
    return answer

n, horizontal, result = 5, False, [[0,3,4,15,16],[1,6,13,18,31],[8,11,20,29,32],[9,22,27,34,39],[24,25,36,37,40]]
print(solution(n, horizontal))