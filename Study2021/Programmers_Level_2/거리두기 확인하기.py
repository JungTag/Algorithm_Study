# https://programmers.co.kr/learn/courses/30/lessons/81302
ㅁ
from collections import deque

def solution(places):
    SIZE = 5
    answer = []

    for place in places:
        graph = place
        visited = [[0 for _ in range(SIZE)] for _ in range(SIZE)]

        if is_complying(graph, visited, SIZE):
            answer.append(1)
        else:
            answer.append(0)

    return answer


def is_complying(graph, visited, SIZE):
    for i in range(SIZE):
        for j in range(SIZE):
            if graph[i][j] == 'P' and not visited[i][j]:
                if not bfs(graph, visited, i, j, SIZE):
                    return False
    return True


def bfs(graph, visited, startY, startX, SIZE):
    queue = deque([[startY, startX, 0]])
    visited[startY][startX] = 1
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    while queue:
        y, x, dist = queue.popleft()

        if dist < 2:
            visited[y][x] = 1
        else:
            return True

        for i in range(4):
            ny, nx = y+directions[i][0], x+directions[i][1]

            if 0 <= ny < SIZE and 0 <= nx < SIZE:
                if not visited[ny][nx]:
                    if graph[ny][nx] == 'O':
                        queue.append([ny, nx, dist+1])
                    if graph[ny][nx] == 'P':
                        return False
    
    return True

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))