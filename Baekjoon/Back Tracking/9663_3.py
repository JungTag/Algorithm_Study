#내 윗줄에 나와 겹치는 라인에 퀸이 있는가?
def adjacent(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True
        
#한줄씩 재귀하며 DFS를 실행
def dfs(x):
    global result
    
    if x == N:
        result += 1

    else:
        for i in range(N):
            row[x] = i
            if adjacent(x):
                dfs(x + 1)
'''
어차피 윗 줄만 검사하면 되기 때문에
row[x] = i 윗줄을 먼저 확인해주고 인접을 확인한다.
'''


N = int(input())
row = [0] * N
result = 0
dfs(0)
print(result)