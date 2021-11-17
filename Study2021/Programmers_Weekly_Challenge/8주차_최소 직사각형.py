# https://programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    longers = sorted([max(size) for size in sizes])
    shorters = sorted([min(size) for size in sizes])
    answer = longers[-1] * shorters[-1]

    return answer

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))