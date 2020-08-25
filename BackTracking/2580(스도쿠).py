import sys
puzzle = []
for _ in range(9):
    puzzle.append([int(x) for x in sys.stdin.readline().strip().split()])
queue = []
boundary_num = [(0,3), (3,6), (6,9)]

def find_empty_cell():
    for row in range(8,-1,-1):
        for col in range(8,-1,-1):
            if puzzle[row][col] == 0:
                queue.append((row,col))

def is_safe(row, col, num):
    if num in puzzle[row]: # if num in row_set
      return False
    for i in range(9):
      if num == puzzle[i][col]: # if num in col_set
        return False
    # box check
    if row <= 2:
      start_row, end_row = boundary_num[0]
    elif row <= 5:
      start_row, end_row = boundary_num[1]
    else:
      start_row, end_row = boundary_num[2]
    if col <= 2:
      start_col, end_col = boundary_num[0]
    elif col <= 5:
      start_col, end_col = boundary_num[1]
    else:
      start_col, end_col = boundary_num[2]
    for i in range(start_row, end_row):
      for j in range(start_col, end_col):
        if num == puzzle[i][j]:
          return False
    return True

def paint_sudoku():
    if queue:
        row, col = queue.pop()
        for num in range(1,10):
            if is_safe(row, col, num):
                puzzle[row][col] = num
                if paint_sudoku():  # 숫자를 넣고 퍼즐이 모두 채워졌는지 확인한다.
                    return True
        puzzle[row][col] = 0  # 마땅히 넣을 숫자가 없으면 0을 넣고 해당 행과 열을 큐에 삽입한다.
        queue.append((row, col))
        return False
    else: 
    # 여러가지 경우의 수가 있는 퍼즐의 경우 한 가지만 보여주면 되므로 출력 후 프로그램을 종료시킨다.
      for row in puzzle:
        for x in row:
          print(x, end = ' ')
        print()
      sys.exit(0) 

find_empty_cell()
paint_sudoku()