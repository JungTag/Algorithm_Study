def solution(s):
    answer = []
    answer_set = set()
    
    i = 1
    tuple_list = []
    stack = []
    num = ""
    
    while i <= len(s)-2:
        if s[i] == "}":
            stack.append(int(num))
            tuple_list.append(stack)
            stack = []
            num = ""
            i += 1
            continue
        if s[i] != "{" and s[i] != ",":
            num += s[i]
        if s[i] == ",":
            if len(num) >= 1:
                stack.append(int(num))
                num = ""
        i += 1
    
    tuple_list.sort(key=lambda x: len(x))
    
    for x in tuple_list:
        for num in x:
            if num not in answer_set:
                answer.append(int(num))
                answer_set.add(int(num))

    return answer
