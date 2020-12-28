'''
1. 중복을 어떻게 줄일 것인가?
2. 조건문은 최대한 지양(시간 제한)
3. 메모리를 많이 사용하면 안된다.
-> 반복문을 사용할 것
처음 dp테이블 구성을 어떻게 할 것인가?
P[n] = P[n - c1] + P[n - c2] + ... + P[n - cn]
-> P[c1] ~ P[cn]을 다 구해야 함,,
-> 예외가 너무 많음(base case 구성도 어려움)
# 예외처리
동전의 값어치가 만들고자 하는 수보다 클 수도 있음: 동전 제외

'''
import sys
n, k = int(input().split())
coin_list = [int(sys.stdin.readline()) for x in range(n) if int(sys.stdin.readline()) < k]
coin_list.sort
cnt = [None] * (k + 1)
 
def solve(n):
    if n <= coin_list[-1]:

