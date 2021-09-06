def solution(n, lost, reserve):
    answer = 0
    student_dict = {i:(True if i not in lost or i in reserve else False) for i in range(1, n+1)}
    reserve[:] = [x for x in reserve if x not in lost]
    for x in reserve:
        if x-1 in student_dict.keys() and student_dict[x-1] == False:
            student_dict[x-1] = True
            continue
        if x+1 in student_dict.keys() and student_dict[x+1] == False:
            student_dict[x+1] = True
            continue
    for x in student_dict.values():
        if x == True: answer += 1
    return answer

# lost와 reserve 모두에 속해있는 학생이 존재하는 경우를 고려해야 함!