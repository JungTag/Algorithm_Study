def solution(grid, clockwise):
    LEN = len(grid)
    answer = []

    if clockwise:
        turn_clockwise(answer, grid, LEN)
    else:
        turn_unclockwise(answer, grid, LEN)
    
    return

def turn_clockwise(answer, grid, LEN):
    for i in range(LEN):
        row = grid[i][0]
        for j in range(i+1, LEN):
            row += grid[j][2*(j-i)-1:2*(j-i)+1]
        answer.append(row[::-1])
    
    return answer[::-1]

def turn_unclockwise(answer, grid, LEN):
    for i in range(LEN):
        row = grid[i][0]
        for j in range(i+1, LEN):
            row += grid[j][2*(j-i)-1:2*(j-i)+1]
        answer.append(row[::-1])
    
    return answer[::-1]

print(solution(["1","234","56789"], True))
print(solution(["A","MAN","DRINK","WATER11"], False))