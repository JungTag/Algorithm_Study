def solution(name):
    answer = 0
    string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; char_dict = {}; name_to_num = []; current_name = []
    ALPHABET_LEN = len(string); NAME_LEN = len(name); candidate = []
    for i in range(len(string)): char_dict[string[i]] = i+1
    for ch in name:
        name_to_num.append(char_dict[ch])
    for _ in range(NAME_LEN):
        current_name.append(1)

    # right
    answer = cal_control(name_to_num[0], ALPHABET_LEN); current_name[0] = name_to_num[0]
    print("right", answer, char_dict[name[0]])
    for i in range(1, NAME_LEN):
        answer += 1
        if name[i] != 1:
            answer += cal_control(name_to_num[i], ALPHABET_LEN); current_name[i] = name_to_num[i]
        if name_to_num == current_name:
            break
        print("right", answer, char_dict[name[i]])
    candidate.append(answer); current_name = []
    for _ in range(NAME_LEN):
        current_name.append(1)
    # turn left
    for i in range(NAME_LEN):
        answer = cal_control(name_to_num[0], ALPHABET_LEN); current_name[0] = name_to_num[0]
        for j in range(1, i+1):
            answer += 1
            if name[j] != 1:
                answer += cal_control(name_to_num[j], ALPHABET_LEN); current_name[j] = name_to_num[j]
        for k in range(i-1, -NAME_LEN+i, -1):
            answer += 1
            if current_name[k] != name_to_num[k] and name[k] != 1:
                answer += cal_control(name_to_num[k], ALPHABET_LEN); current_name[k] = name_to_num[k]
            if name_to_num == current_name:
                break
        candidate.append(answer); current_name = []
        for _ in range(NAME_LEN):
            current_name.append(1)
    answer = min(candidate)

    return answer

def cal_control(char, ALPHABET_LEN):
    if char <= ALPHABET_LEN//2 + 1:
        return char - 1
    else:
        return (ALPHABET_LEN + 1) - char
'''
11번 케이스
print(solution("BBBAAAB")) # 9
print(solution("ABABAAAAABA")) # 11
'''

# def solution(name):
#     answer = 0
#     string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"; char_dict = {}; name_to_num = []; current_name = []
#     ALPHABET_LEN = len(string); NAME_LEN = len(name)
#     for i in range(len(string)): char_dict[string[i]] = i+1
#     for ch in name:
#         name_to_num.append(char_dict[ch])
#     for _ in range(NAME_LEN):
#         current_name.append(1)

#     if name_to_num[:NAME_LEN//2+1].count(1) < name_to_num[NAME_LEN//2+1:].count(1):
#         answer += cal_control(name_to_num[0], ALPHABET_LEN); current_name[0] = name_to_num[0]
#         print("right", answer, char_dict[name[0]])
#         for i in range(1, NAME_LEN):
#             answer += 1
#             if name[i] != 1:
#                 answer += cal_control(name_to_num[i], ALPHABET_LEN); current_name[i] = name_to_num[i]
#             if name_to_num == current_name:
#                 break
#             print("right", answer, char_dict[name[i]])
#     else:
#         answer += cal_control(name_to_num[0], ALPHABET_LEN); current_name[0] = name_to_num[0]
#         print("left", answer, char_dict[name[0]])
#         for i in range(-1, -NAME_LEN, -1):
#             answer += 1
#             if name[i] != 1:
#                 answer += cal_control(name_to_num[i], ALPHABET_LEN); current_name[i] = name_to_num[i]
#             if name_to_num == current_name:
#                 break
#             print("left", answer, char_dict[name[i]])

#     return answer

