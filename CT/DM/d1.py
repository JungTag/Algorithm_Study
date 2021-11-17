def solution(registered_list, new_id):
    answer = new_id
    registered_set = set(registered_list)

    while answer in registered_set:
        numeric_start_index = get_first_numeric_index(answer)
        if numeric_start_index == -1:
            answer += '1'
        else:
            answer = answer[:numeric_start_index] + str(int(answer[numeric_start_index:]) + 1)

    return answer

def get_first_numeric_index(string):
    for i, char in enumerate(string):
        if char.isdigit():
            return i
    return -1

print(solution(	["bird99", "bird98", "bird101", "gotoxy"], "bird98"))