def solution(logs):
    MIN_PROBLEM_NUM = 5

    answer = set([])
    student_dict = {}

    # 이차원 딕셔너리 형태로 점수를 관리한다.
    for log in logs:
        student_num, problem_num, score = log.split()
        if student_num in student_dict.keys():
            student_dict[student_num][problem_num] = score
        else:
            student_dict[student_num] = {problem_num: score}

    student_num_list = list(student_dict.keys())
    len_of_list = len(student_num_list)

    for i in range(len_of_list-1):
        student1 = student_num_list[i]
        
        if len(student_dict[student1]) < MIN_PROBLEM_NUM:
            continue

        for j in range(i+1, len_of_list):
            student2 = student_num_list[j]

            if len(student_dict[student2]) < MIN_PROBLEM_NUM:
                continue

            if len(student_dict[student1]) != len(student_dict[student2]):
                continue

            is_cheating = True

            # 두 수험자가 푼 문제의 번호와 점수가 모두 일치하는지 확인한다.
            for problem_num, score in student_dict[student1].items():
                if problem_num in student_dict[student2]:
                    if score != student_dict[student2][problem_num]:
                        is_cheating = False
                        break
                else:
                    break
            
            if is_cheating == True:
                answer.add(student1)
                answer.add(student2)

    if answer:
        answer = sorted(list(answer))
    else:
        answer = ["None"]

    return answer

# print(solution(["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80", "0001 8 80", "0001 10 90", "0002 10 90", "0002 7 80", "0002 8 80", "0002 5 100", "0003 99 90"]))
print(solution(["1901 1 100", "1901 2 100", "1901 4 100", "1901 7 100", "1901 8 100", "1902 2 100", "1902 1 100", "1902 7 100", "1902 4 100", "1902 8 100", "1903 8 100", "1903 7 100", "1903 4 100", "1903 2 100", "1903 1 100", "1101 1 95", "1101 2 100", "1101 4 100", "1101 7 100", "1101 9 100", "1102 1 95", "1102 2 100", "1102 4 100", "1102 7 100", "1102 9 100"]))