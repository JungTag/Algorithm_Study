'''
1차원 리스트로 만들면 한계가 있다(최적해가 안 구해짐)
2차원 리스트로 만들고 현재 행과 윗 행의 요소를 비교하여 테이블을 채운다.
'''
import sys
N, K = map(int, sys.stdin.readline().split())
knap_list = []
for _ in range(N):
    W, V = map(int, sys.stdin.readline().split())
    if W <= K:  # 배낭의 무게가 K보다 클 경우 해당 아이템을 빼준다.
        knap_list.append((W, V))
knap_list.sort(key = lambda x : (x[0], x[1]))

DP = [[0 for _ in range(K+1)] for _ in range(len(knap_list))]

if knap_list:
    first_weight, first_value = knap_list[0][0], knap_list[0][1]
    DP[0][first_weight] = first_value

    for i in range(1, len(knap_list)):
        DP[i] = DP[i-1][:]
        weight, value = knap_list[i][0], knap_list[i][1]
        for j in range(weight, K+1):
            if DP[i-1][j-weight] != 0:
                DP[i][j] = max(DP[i][j], DP[i-1][j-weight] + value)  # max(DP[i][j], DP[i-1][j-weight] + DP[i][weight]) 
        if DP[i][weight] < value: 
            DP[i][weight] = value

    print(max(DP[len(knap_list)-1]))  # K보다 훨씬 낮은 무게에서 최대 가치가 발생할 수 있다.

else: # 예외 처리: 아이템이 단 하나인데 무게가 K보다 큰 경우
    print(0)