def solution(s):
    LEN = len(s)

    answer = []
    cnt = 1

    for i in range(1, LEN):
        if s[i-1] == s[i]:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
        if i == LEN-1:
            answer.append(cnt)

    if s[0] == s[LEN-1]:
        answer[0] += answer.pop()

    answer.sort()

    return answer

# print(solution("aaabbaaa"))
# print(solution("wowwow"))

