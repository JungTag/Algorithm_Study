from collections import defaultdict

def solution(id_list, k):
    answer = 0
    id_dict = defaultdict(int)

    for customers in id_list:
        today = set([])
        for id in customers.split(' '):
            if id not in today:
                id_dict[id] += 1
                today.add(id)

    for cnt in id_dict.values():
        if cnt > k:
            answer += k
        else:
            answer += cnt

    return answer