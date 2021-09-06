# https://www.acmicpc.net/problem/1541
import sys

def make_queue():
    temp = ''
    queue = []
    for i, char in enumerate(formula):
        if char == '+' or char == '-':
            queue.extend([temp, char])
            temp = ''
        else:
            temp += char
    queue.append(temp)
    return queue

def cal_queue():
    status = '+'
    result = 0
    for char in queue:
        if status == '-':
            if char.isdigit(): # 숫자이면
                result -= int(char)
        else:
            if char.isdigit():
                result += int(char)
            elif char == '-':
                status = '-'     
    return result

formula = sys.stdin.readline().strip()
queue = make_queue()
print(cal_queue())
