from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def solution(letters):
    max_depth = len(letters)
    answer = []
    visited = set()
    letter_dict = defaultdict(int)
    
    for letter in letters:
        letter_dict[letter] += 1

    for letter in letters:
        letter_dict[letter] -= 1
        dfs(max_depth, 1, letter, letter_dict, visited, answer)
        letter_dict[letter] += 1

    return sorted(answer)


def dfs(max_depth, cur_depth, cur_letter, letter_dict, visited, answer):
    visited.add(cur_letter)
    
    if cur_depth == max_depth:
        answer.append(cur_letter)
        return
    
    for letter, cnt in letter_dict.items():
        if cnt > 0:
            if (cur_letter + letter not in visited) and (cur_letter[-1] != letter):
                letter_dict[letter] -= 1
                dfs(max_depth, cur_depth+1, cur_letter+letter, letter_dict, visited, answer)
                letter_dict[letter] += 1


print(solution("abca"))
print(solution("abcbc"))

