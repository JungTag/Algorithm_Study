# https://www.acmicpc.net/problem/16918
import sys


def solution(r, c, n, board):
    time = 1
    check_board(r, c, board)

    while time < n:
        time += 1
        if time % 2 == 0:
            set_bombs(r, c, board)
        check_board(r, c, board)

    format_board(r, c, board)


def set_bombs(r, c, board):
    for i in range(r):
        for j in range(c):
            if board[i][j] == '.':
                board[i][j] = -1


def check_board(r, c, board):
    EXPLOSION_TIME = 3

    for i in range(r):
        for j in range(c):
            if board[i][j] != '.':
                board[i][j] += 1

    for i in range(r):
        for j in range(c):
            if board[i][j] == EXPLOSION_TIME:
                exlplode(i, j, r, c, board)


def exlplode(y, x, r, c, board):
    EXPLOSION_TIME = 3

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    board[y][x] = '.'

    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0 <= ny < r and 0 <= nx < c:
            if board[ny][nx] != EXPLOSION_TIME:
                board[ny][nx] = '.'


def format_board(r, c, board):
    for i in range(r):
        for j in range(c):
            if board[i][j] != '.':
                board[i][j] = 'O'
        board[i] = ''.join(board[i])

    for i in range(r):
        print(board[i])


input = sys.stdin.readline
r, c, n = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]

for i in range(r):
    for j in range(c):
        if board[i][j] == 'O':
            board[i][j] = 0

solution(r, c, n, board)