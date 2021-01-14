from itertools import combinations
import sys

while True:
    input = [int(x) for x in sys.stdin.readline().split()]
    k = input[0]
    if k == 0:
        break
    input = input[1:]

    combis = list(combinations(input, 6))
    for combi in combis:
        print(*combi)
    print()