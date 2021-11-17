def solution(rows, columns):
    answer = [[0 for _ in range(columns)] for _ in range(rows)]
    next = [[[-1, -1] for _ in range(columns)] for _ in range(rows)] # 다음에 이동할 좌표를 저장한다.

    r, c = 0, 0
    num = 0

    while not is_no_zero(answer, rows, columns):
        num += 1
        answer[r][c] = num
        nr, nc = r, c

        if num % 2 == 0:
            if r == rows - 1:
                nr = 0
            else:
                nr = r + 1
        else:
            if c == columns - 1:
                nc = 0
            else:
                nc = c + 1
        
        if not is_repeated(next, r, c, nr, nc):
            next[r][c] = [nr, nc]
            r, c = nr, nc
        else:
            answer[r][c] -= num-1
            break

    return answer


def is_no_zero(answer, rows, columns):
    for i in range(rows):
        for j in range(columns):
            if answer[i][j] == 0:
                return False
    return True


def is_repeated(next, r, c, nr, nc):
    # 이전에 이동했던 좌표와 다음에 이동할 좌표가 같다면 사이클이 발생하게 된다.
    if next[r][c][0] == nr and next[r][c][1] == nc:
        return True
    return False
    

print(solution(3, 4))