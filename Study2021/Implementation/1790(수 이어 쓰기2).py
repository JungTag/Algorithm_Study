# https://www.acmicpc.net/problem/1790
# https://kyu9341.github.io/algorithm/2020/03/03/algorithm1790/
# https://bgpark.tistory.com/112
import sys

def solve():
    if calc(n) < k:
        return - 1
    left, right = 1, n
    ans = 0
    while (left <= right): # 어떤 수까지 이어 써야 k번째 수가 나오는지 확인
        mid = (left + right) // 2
        total_len = calc(mid) # mid -> 어떤 수
        if (total_len < k):
            left = mid + 1
        else:
            ans = mid
            right = mid - 1
    s = str(ans)
    l = calc(ans)
    return s[len(s) - (l - k) - 1]


def calc(t): # t까지의 수를 모두 이어 썼을 때 그 수의 길이
    ans = 0 # 수의 길이
    start = 1 # 자리수의 첫 수(1, 10, 100, ...)
    len = 1 # 숫자 하나당 길이
    while (start <= t):
        end = start*10 - 1 # 자리수의 마지막 수(9, 99, 999, ...)
        if (end >= t):
            ans += (t-start+1) * len
        else:
            ans += (end-start+1) * len # +9 , +90, +900, ...
        start *= 10
        len += 1
    return ans

input = sys.stdin.readline
n, k = map(int, input().split())
print(solve())