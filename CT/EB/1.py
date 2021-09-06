from collections import deque

def solution(s):
    MAX = len(s)
    answer = MAX
    left, right = 1, answer
    while left <= right:
        mid = (left+right) // 2
        if is_possible(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer

def is_possible(target, s, MAX):
    check_set = set(["01", "10"])
        
                


s = input()
print(solution(s))