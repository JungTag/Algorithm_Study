# https://www.acmicpc.net/problem/1759
import sys
from itertools import combinations

def make_code():
    result = []
    for c in list(combinations(chars, l)):
        vowel_cnt = consonants_cnt = 0
        for char in c:
            if char in vowels:
                vowel_cnt += 1
            else:
                consonants_cnt += 1
        if vowel_cnt > 0 and consonants_cnt > 1:
            result.append("".join(c))
    return result

l, c = map(int, sys.stdin.readline().split())
chars = sorted(sys.stdin.readline().split())

vowels = set(['a', 'e', 'i', 'o', 'u'])

for p in make_code():
    print(p)
