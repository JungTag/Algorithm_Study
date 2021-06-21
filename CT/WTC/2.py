def solution(s, op):
    answer = []
    for i in range(1, len(s)):
        if op == "+":
            result = int(s[:i]) + int(s[i:])
        elif op == "-":
            result = int(s[:i]) - int(s[i:])
        else:
            result = int(s[:i]) * int(s[i:])
        answer.append(result)

    return answer