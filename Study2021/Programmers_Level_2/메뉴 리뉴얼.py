# https://programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
    max_set = defaultdict(int) # {len: cnt}
    course_dict = defaultdict(int)

    for order in orders:
        order = ''.join(sorted(order))
        for num in course:
            if len(order) < num:
                break
            for combi in list(combinations(order, num)):
                new_course = make_new_course(combi)
                course_dict[new_course] += 1
                max_set[len(new_course)] = max(max_set[len(new_course)], course_dict[new_course])

    for course, count in course_dict.items():
        if count >= 2 and count == max_set[len(course)]:
            answer.append(course)

    return sorted(answer)


def make_new_course(tuple):
    result = ''
    for char in tuple:
        result += char

    return result

'''
1. 조합이용
for o in orders:
    for n in course:
        n = 2 (가짓수)
        if len(o) >= n:
            o에서 n개 뽑아서 조합 만들고 dict에 추가
            if 해당 조합 in dict:
                dict[조합] += 1
            else:
                dict[조합] = 0

for k, v in dict:
    if v >= 2 and v가 해당 가짓수에 최댓값인지 확인:
        answer.append(k)
'''