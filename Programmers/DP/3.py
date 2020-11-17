def solution(m, n, puddles):
    G = [[[0,0] for _ in range(m+2)] for _ in range(n+2)];G[1][1] = [0,1] #(거리, 경우)
    # G = [[[0,0]] * m] * n -> 이렇게 만들면 이상해짐(참조문제 발생)
    for co in puddles:
        x, y = co[0], co[1]
        G[x][y] = [-1,-1]
    for x in range(1, n):
        for y in range(1, m):
    answer = G[n][m][1] % 1000000007
    return answer


solution(4, 3, [[2,2]])