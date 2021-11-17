def solution(board):
    SIZE = len(board)

    max_zero_y = [-1, -1] # [y,x]
    max_zero_x = [-1, -1] # [y,x]

    dp = [[0 for _ in range(SIZE+1)] for _ in range(SIZE+1)]

    dp[1][1] = board[0][0]

    # 0의 최대 영역을 구해준다.
    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] == 0:
                if i > max_zero_y[0]:
                    max_zero_y = [i, j]
                if j > max_zero_x[1]:
                    max_zero_x = [i, j]

    for i in range(1, SIZE+1):
        for j in range(1, SIZE+1):
            if i <= max_zero_y[0] and j <= max_zero_x[1]:
                # 0의 최대 영역 안에 있다면 절대값을 크게 만든다.
                if board[i-1][j-1] != 0:
                    if i == 1:
                        dp[i][j] = board[i-1][j-1] + dp[i][j-1]
                        continue
                    if j == 1:
                        dp[i][j] = board[i-1][j-1] + dp[i-1][j]
                        continue
                    
                    c1, c2 = abs(board[i-1][j-1] + dp[i-1][j]), abs(board[i-1][j-1] + dp[i][j-1])
                    
                    if c1 > c2:
                        dp[i][j] = board[i-1][j-1] + dp[i-1][j]
                    else:
                        dp[i][j] = board[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = max(abs(dp[i-1][j]), abs(dp[i][j-1]))
            else:
                # 0의 최대 영역 바깥에 있다면 값을 크게 만든다(양수).
                dp[i][j] = board[i-1][j-1] + max(dp[i-1][j], dp[i][j-1])

    answer = dp[SIZE][SIZE]
    
    return answer


print(solution([[1, -7, -2, 1, -1],[2, 3, 0, -1, -2],[1, -1, 6, -1, -2],[-1, 1, -2, 0, 4],[-10, 5, -3, -1, 1]]))
print(solution([[-10, 20, 30],[-10, 0, 10],[-20, 40, 1]]))