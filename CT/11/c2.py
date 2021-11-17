from collections import defaultdict
from string import ascii_lowercase

def solution(S):
    LEN = len(S)
    answer = []

    word_dict = defaultdict(lambda: defaultdict(set))
    alphabets = list(ascii_lowercase)
    
    for word in S:
        for i, alphabet in enumerate(word):
            word_dict[word][alphabet].add(i)

    for i in range(LEN):
        for j in range(i+1, LEN):
            word1 = S[i]
            word2 = S[j]

            for alphabet in alphabets:
                if alphabet in word_dict[word1] and alphabet in word_dict[word2]: # 해당 알파벳이 각 문자열에 속하는지 && 같은 인덱스에 존재하는지 검사
                    same_indexes = list(word_dict[word1][alphabet] & word_dict[word2][alphabet])
                    if len(same_indexes) > 0:
                        return [i, j, same_indexes[0]]
    
    return answer


print(solution(['abc', 'bca', 'dbe']))