def solution(progresses, speeds):
    answer = []
    days = [0] * len(speeds)
    for i in range(len(speeds)):
        days[i] = (100 - progresses[i]) // speeds[i]
        if ((100 - progresses[i]) % speeds[i]) != 0:
            days[i] += 1
    i = 0
    while True:
        temp, escape = 1, False
        for j in range(i+1, len(days)+1):
            try:
                if days[i] >= days[j]:
                    temp += 1
                else:
                    answer.append(temp)
                    i = j
                    break
            except IndexError:
                answer.append(temp)
                escape = True
        if escape == True:
            break
    return answer