import sys
puzzle = []
for _ in range(9):
    puzzle.append([int(x) for x in sys.stdin.readline().strip().split()])
queue = []
boundary_num = [(0,3), (3,6), (6,9)]

def find_empty_cell():
    # range(9)로 돌리면 시간초과가 나온다. 아무래도 is_safe에서 윗열부터 검사하기 때문인 것 같다..?
    for row in range(8,-1,-1): 
        for col in range(8,-1,-1):
            if puzzle[row][col] == 0:
                queue.append((row,col))

def is_safe(row, col, num):
    # row check
    if num in puzzle[row]:
      return False
    # column check
    for i in range(9):
      if num == puzzle[i][col]:
        return False
    # box(3x3) check
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
            if is_safe(row, col, num):  # 가로, 세로, 3x3 검사를 해서 숫자 삽입이 가능한지 여부를 확인한다.
                puzzle[row][col] = num
                paint_sudoku()  
        puzzle[row][col] = 0  # 마땅히 넣을 숫자가 없으면 0을 넣고 해당 행과 열을 큐에 삽입한다.
        queue.append((row, col))
    else: 
    # 여러가지 경우의 수가 있는 퍼즐의 경우 한 가지만 보여주면 되므로 출력 후 프로그램을 종료시킨다.
      for row in puzzle:
        print(*row)
      sys.exit(0) 

find_empty_cell()
paint_sudoku()