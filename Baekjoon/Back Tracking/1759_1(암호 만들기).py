# https://www.acmicpc.net/problem/1759
import sys

def make_code(cur, depth, p):
    result = []
    if depth == l:
        if len(set(p) & vowels) > 0 and len(set(p) & consonants) > 1:
            return ["".join(p)]
    else:
        for i in range(cur, c):
            result += make_code(i+1, depth+1, p+[chars[i]])
    return result

l, c = map(int, sys.stdin.readline().split())
chars = sorted(sys.stdin.readline().split())

vowels = set(['a', 'e', 'i', 'o', 'u'])
consonants = set([x for x in chars if x not in vowels])

for p in make_code(0, 0, []):
    print(p)
