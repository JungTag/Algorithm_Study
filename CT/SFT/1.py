import sys

def solution(s):
    energy = 0
    cnt = 0

    while s >= 1:
        s /= 2
        energy += 2 ** cnt
        cnt += 1

    return energy 


input = sys.stdin.readline()
s = int(input.strip())

print(solution(s))


