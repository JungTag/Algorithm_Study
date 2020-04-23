cnt = [None] * 1000001
cnt[1] = 0
cnt[2] = cnt[3] = 1

def min(n): 
    if cnt[n] != None: return cnt[n]
    if n % 6 == 0:
        if min(n // 3) > min(n // 2):
            cnt[n] = min(n // 2) + 1
            return cnt[n]
        else:
            cnt[n] = min(n // 3) + 1
            return cnt[n]
    elif n % 3 == 0:
        if min(n - 1) > min(n // 3): 
            cnt[n] = min(n // 3) + 1
            return cnt[n]
        else:
            cnt[n] = min(n - 1) + 1
            return cnt[n]
    elif n % 2 == 0:
        if min(n // 2) > min(n - 1): 
            cnt[n] = min(n - 1) + 1
            return cnt[n]
        else:
            cnt[n] = min(n // 2) + 1
            return cnt[n]
    else:
        cnt[n] = min(n - 1) + 1
        return cnt[n]

n = int(input())
print(min(n))

'''풀이
1) 처음 했던 아이디어
a- 최적의 규칙을 찾아서 해결한다.
b- 재귀 구조를 이용한다

2) a - 방법대로 최적의 규칙을 찾아서 해결하려 했다.
ex) 
3의 배수면 무조건 3으로 나누고 
2의 배수면 n - 1을 3으로 얼마나 나눌 수 있는지와 n을 2로 얼마나 나눌 수 있는지 비교해서 1을 빼거나 2로 나눴다.
-> 작은 수에서는 되지만 수가 커질수록 맞지 않음(반례가 많음)

3) b - 재귀 구조를 이용했다.
처음에 재귀 구조를 이용하려 했더니, 너무 많은 연산시간이 소요됐다.
그래서 배열을 선언해서 이미 계산한 값을 저장하도록 했다. 그 와중에 배열 cnt를 1000000짜리로 만들어서 컴파일 에러가 발생했다.
(n으로 인덱스 접근을 하기 위해서는 1000001짜리로 만들어야 한다.)
처음에 min(n // 3)과 (n - 1)을 비교하지 않아서 반례가 발생했다.
그 후엔 스택 오버플로우가 계속 발생했는데 재귀 제한을 풀어도 해결되지 않았다.

4) 해결
많은 재귀를 불러일으키는 min(n - 1)을 줄이기 위해 n이 6이 배수일 시 min(n // 2)와  min(n // 3) 연산 둘 중 하나를 선택해서 하도록 했다.
그래도 계속 안 돼서 확인해보니 cnt[1]에 1을 대입해서 계속 오류가 발생했던 거였다...
'''