# https://programmers.co.kr/learn/courses/30/lessons/84512

import sys
sys.setrecursionlimit(10**6)

def solution(word):
    global cnt
    global answer

    answer = 0
    cnt = 0
    alphabets = ['A', 'E', 'I', 'O', 'U']
    visited = set([])

    def dfs(cur):
        global cnt
        global answer

        visited.add(cur)
        cnt += 1

        if cur == word:
            answer = cnt
            return

        if len(cur) >= 5:
            return

        for alphabet in alphabets:
            _next = cur + alphabet
            if _next not in visited:
                dfs(_next)
    
    for alphabet in alphabets:
        dfs(alphabet)
    
    return answer

print(solution("I"))

'''
[A, E, I, O, U]
A, AA, AAA, AAAA, AAAAA, AAAAE, AAAAI, AAAAO, AAAAU, ...
10000, 11000, 11100, 11110, 11111, 11112, 11113, 11114, 11115,
AAAE, AAAEA, AAAEE, AAAEI, AAAEO, AAAEU
11120, 11121, 11122, 11123, 11124, 11125
AAE, AAEA, AAEI, AAEO, AAEU
11200, 11210, 11220, 11230, 11240

1) 반복문 더하면서 붙이기..? -> 자리수가 절대적인 게 아님!
2) 딕셔너리 형태,,?
['A': 1, 'E': 2, 'I': 3, 'O': 4, 'U': 5]

3) DFS..?
A dep = 1, *10000
A E I O U dep = 2, *1000
A E I O U

alphabets = ['A', 'E', 'I', 'O', 'U']
'''