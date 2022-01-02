import sys

def solution(n, cars):
    cars_list = [[i+1, car] for i, car in enumerate(cars)]
    result = [x[0] for x in sorted(cars_list, key = lambda x: (x[1]))]
    return result


input = sys.stdin.readline
n = int(input().strip())
cars = [int(x) for x in input().split()] 

print(*solution(n, cars))