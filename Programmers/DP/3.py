def solution(m, n, puddles):
    G = [[0 for _ in range(m+1)] for _ in range(n+1)]
    G[1][1] = 1 
    NUM = 1000000007

    for co in puddles:
        x, y = co[0], co[1]
        G[y][x] = -1

    for x in range(1, n+1):
        for y in range(1, m+1):
            if G[x][y] == -1:
                G[x][y] = 0 
            else:
                G[x][y] += G[x-1][y] + G[x][y-1] 

    answer = G[n][m] % NUM
    return answer

# 효율성은 풀이2가 더 나음
# G = [[[0,0]] * m] * n -> 이렇게 만들면 이상해짐(참조문제 발생)

''' 풀이2
def solution(m, n, puddles):
    G = [[0 for _ in range(m+1)] for _ in range(n+1)]
    G[1][1] = 1 
    NUM = 1000000007

    for x in range(1, n+1):
        for y in range(1, m+1):
            if [y, x] in puddles:
                G[x][y] = 0
            else:
                G[x][y] += G[x-1][y] + G[x][y-1] 

    answer = G[n][m] % NUM
    return answer
'''

''' 풀이1
def solution(m, n, puddles):
    G = [[0 for _ in range(m+1)] for _ in range(n+1)]
    G[1][1] = 1 
    NUM = 1000000007

    for co in puddles:
        x, y = co[0], co[1]
        G[y][x] = -1

    for x in range(1, n+1):
        for y in range(1, m+1):
            if G[x][y] == -1:
                G[x][y] = 0 
                continue
            if x != 1:
                G[x][y] += G[x-1][y] % NUM
            if y != 1:
                G[x][y] += G[x][y-1] % NUM

    answer = G[n][m] % NUM
    return answer
'''