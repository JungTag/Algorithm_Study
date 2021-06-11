def solution(logs):
    answer = []; std_dict = {}

    for i in range(len(logs)):
        dummy, pro_num, score = map(int, logs[i].split())
        std_num = logs[i][:4]
        if std_num in std_dict.keys():
            std_dict[std_num][pro_num] = score
        else:
            std_dict[std_num] = {pro_num: score}

    key_list = list(std_dict.keys())
    for i in range(len(key_list)-1):
        std1 = key_list[i]
        if len(std_dict[std1]) < 5: continue
        for j in range(i+1, len(key_list)):
            esc = False
            std2 = key_list[j]
            # 문제 수 일치 확인
            if len(std_dict[std2]) < 5 or len(std_dict[std1]) != len(std_dict[std2]): 
                continue
            # 문제 번호 및 점수 확인
            for key, value in std_dict[std1].items():
                if key in std_dict[std2]:
                    if value != std_dict[std2][key]:
                        esc = True
                        break
            if esc == True: continue
            answer.extend([std1, std2])
    if not answer: answer.append("None")
    else: answer = sorted(list(set(answer)))
    return answer

logs = ["0001 3 95", "0001 5 90", "0001 5 100", "0002 3 95", "0001 7 80", "0001 8 80", "0001 10 90", "0002 10 90", "0002 7 80", "0002 8 80", "0002 5 100", "0003 99 90"]
print(solution(logs))

a = set()
a.add(("1","2"))
print(a)