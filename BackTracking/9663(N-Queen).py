def adjacent(k):
    for i in range(k):
        if row[k] == row[i] or abs(row[k] - row[i]) == k - i:
            return False
    return True
        
        
def back_track(k):
    global result
    
    if k == N:
        result += 1

    else:
        # N이 짝수일 떄, 절반만 계산해준다(대칭이므로)
        if k == 0 and N % 2 == 0:
            for i in range(N//2):
                row[0] = i
                if adjacent(k):
                    back_track(k + 1)
            print(result*2)

        # N이 짝수일 떄, 절반 + 중앙까지 계산해준다
        elif k == 0 and N % 2 == 1:
            for i in range(N//2):
                row[0] = i
                if adjacent(k):
                    back_track(k + 1)
            half = result
            row[0] = N//2
            if adjacent(k):
                back_track(k+1)
            including_center = result            
            print(half*2 + including_center - half)

        # 일반적인 연산
        else:
            for i in range(N):
                row[k] = i
                if adjacent(k):
                    back_track(k + 1)

N = int(input())
row = [0] * N
result = 0
back_track(0)

'''
틀린 코드 -> 리스트 복제하는 데 너무 많은 시간이 소요됨
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
    for candidate_column in range(n):
        if check_board(row+1, candidate_column, solution):
            back_track(row+1, candidate_column, copy.copy(solution))
            
# 윗 줄만 확인하면 되는데 아랫줄까지 확인하고 있었음...
def check_board(row, column, solution):
    same_column_set = set(solution)
    if column in same_column_set:
        return False
        
    cnt = 0
    for pre_row in range(row-1, -1, -1):
        cnt += 1
        if solution[pre_row] is not None: 
        # solution[pre_row] -> 해당 행에서 퀸이 어느 열에 위치하는가를 담고 있음
            if column - cnt == -1:
                break
            if solution[pre_row] == column - cnt:
                return False
        else:
            break

    cnt = 0
    for pre_row in range(row-1, -1, -1):
        cnt += 1
        if solution[pre_row] is not None:
            if column + cnt == n:
                break
            if solution[pre_row] == column + cnt:
                return False
        else:
            break

    return True

for column in range(n//2):
    solution = [None for _ in range(n)]
    back_track(FIRST_ROW, column, solution)

if n % 2 == 0:
    print(sum * 2)
else:
    half_sum = sum
    solution = [None for _ in range(n)]
    back_track(FIRST_ROW, n//2, solution) # 중앙 라인의 sum을 구하기 위해서
    center_sum = sum - half_sum
    print(half_sum*2 + center_sum)
'''