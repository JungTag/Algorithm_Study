# https://www.acmicpc.net/problem/1339
import sys
from collections import defaultdict

def solve():
    result = 0
    cnt = 9
    for string in strings:
        LEN_OF_STR = len(string)
        for i in range(LEN_OF_STR):
            char = string[i]
            char_dict[char] += 10**(LEN_OF_STR - i - 1)
    for k, v in sorted(char_dict.items(), key = lambda x: x[1], reverse = True):
        result += v * cnt
        cnt -= 1
    return result

# init
input = sys.stdin.readline
n = int(input().strip())
strings= [input().strip() for _ in range(n)]
char_dict = defaultdict(int)

print(solve())