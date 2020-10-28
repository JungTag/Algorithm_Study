import sys
from collections import deque
n = int(sys.stdin.readline().strip())
W = deque([int(sys.stdin.readline().strip()) for _ in range(n)])
for _ in range(3):
    W.appendleft(0)
DP = [0] * (n+3)

for i in range(3, n+3):
    DP[i] = max(DP[i-3]+W[i-1]+W[i], DP[i-2]+W[i], DP[i-1])
print(DP[-1])

'''
아이디어
1) 연속 2칸이 안되는 문제
DP[i]를 구하는 데에 있어 DP[i-1], DP[i-2]가 부분해
=> 연속 3칸이 안되는 문제에선 DP[i-1], DP[i-2], DP[i-3]이 부분해가 되지 않을까?
2) 계단문제처럼 연속 3칸이 되는 상황을 피하는 점화식을 세운다.
=> 1칸의 공백을 만든다


참고한 반례)
발견한 문제점: 계단과 달리 비연속적 가능
6
4
5
1
1
16
15
'''