from collections import defaultdict

def solution(arr):
    answer = []
    num_dict = {1: 0, 2: 0, 3: 0}

    for num in arr:
        num_dict[num] += 1

    max_cnt = max(num_dict.values())

    for cnt in num_dict.values():
        answer.append(max_cnt - cnt)

    return answer