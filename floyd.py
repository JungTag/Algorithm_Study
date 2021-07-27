# 리스트는 인접 행렬 형태로 표현
n, m = map(int, input())
g = [] # 3차원 리스트라고 가정

for mid in range(1, n+1):
    for start in range(1, n+1):
        for end in range(1, n+1):
            g[start][end] = min(g[start][end], g[start][mid] + g[mid][end])

