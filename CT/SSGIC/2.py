def solution(grid):
    answer = -1
    move_col(grid, 'up', 1)

    return answer


def move_row(grid, dir, row):
    SIZE = 4

    if dir == 'left':
        temp = grid[0]
        for i in range(1, 3):
            pass
    else:
        pass


def move_col(grid, dir, c):
    SIZE = 4

    if dir == 'up':
        grid[0][c], grid[1][c], grid[2][c], grid[3][c] = grid[1][c], grid[2][c], grid[3][c], grid[0][c]
    else:
        grid[1][c], grid[2][c], grid[3][c], grid[0][c] = grid[0][c], grid[1][c], grid[2][c], grid[3][c] 

solution()