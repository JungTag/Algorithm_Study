import sys
import copy
n = int(sys.stdin.readline().strip())
FIRST_ROW = 0
sum = 0 # 경우의 수를 저장할 변수

def back_track(row, column, solution):
    global sum
    solution[row] = column
    if row >= n-1:
        sum += 1
        return # get solution
    for candidate_column in range(n):
        next_row = row + 1
        if check_board(next_row, candidate_column, solution):
            added_solution = copy.copy(solution)
            back_track(next_row, candidate_column, added_solution)
            # print(solution, added_solution, next_row)

def check_board(row, column, solution):
    same_column_set = set(solution)
    if column in same_column_set:
        return False

    cnt = 0
    for pre_row in range(row-1, -1, -1):
        cnt += 1
        checked_column = solution[pre_row]
        if checked_column is not None:
            if column - cnt == -1:
                break
            if checked_column == column - cnt:
                return False
        else:
            break

    cnt = 0
    for pre_row in range(row-1, -1, -1):
        cnt += 1
        checked_column = solution[pre_row]
        if checked_column is not None:
            if column + cnt == n:
                break
            if checked_column == column + cnt:
                return False
        else:
            break
        
    cnt = 0
    for post_row in range(row+1, n):
        cnt += 1
        checked_column = solution[post_row]
        if checked_column is not None:
            if column - cnt == -1:
                break
            if checked_column == column - cnt:
                return False
        else:
            break

    cnt = 0
    for post_row in range(row+1, n):
        cnt += 1
        checked_column = solution[post_row]
        if checked_column is not None:
            if column + cnt == n:
                break
            if checked_column == column + cnt:
                return False
        else:
            break

    return True

for column in range(n):
    solution = [None for _ in range(n)]
    back_track(FIRST_ROW, column, solution)

print(sum)