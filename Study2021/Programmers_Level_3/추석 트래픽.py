# https://programmers.co.kr/learn/courses/30/lessons/17676
from collections import defaultdict

def parse_to_sec(line):
    T = 60
    splitted_line = line.split(' ')
    required_time = float(splitted_line[2][:-1])

    h, m, s = splitted_line[1].split(':')
    end = int(h) * T ** 2 + int(m) * T + float(s)
    start = round(end - required_time + 0.001, 3)

    return start, end

def solution(lines):
    answer = 0
    endpoints = set()
    task_dict = defaultdict(int)
    new_lines = []

    for line in lines:
        start, end = parse_to_sec(line)
        endpoints.add(start)
        endpoints.add(end)
        new_lines.append([start, end])

    for endpoint in list(endpoints):
        second_start, second_end = endpoint, round(endpoint + 0.999, 3)
        for line in new_lines:
            start_time, end_time = line
            if not (end_time < second_start or start_time > second_end):
                task_dict[endpoint] += 1

    answer = max(task_dict.values())

    return answer