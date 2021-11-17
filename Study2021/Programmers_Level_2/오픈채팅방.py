# https://programmers.co.kr/learn/courses/30/lessons/42888
from collections import defaultdict

def solution(record):
    answer = []
    user_dict = defaultdict(str)

    for string in record:
        splitted_string = string.split(' ')
        action, user_id = splitted_string[0], splitted_string[1]
        
        if action == 'Enter' or action == 'Change':
            user_name = splitted_string[2]
            user_dict[user_id] = user_name

    for string in record:
        splitted_string = string.split(' ')
        action, user_id = splitted_string[0], splitted_string[1]
        user_name = user_dict[user_id]
        
        if action == 'Enter' or action == 'Leave':
            answer.append(getFormattedString(action, user_name))

    return answer

def getFormattedString(action, user_name):
    if action == 'Enter':
        return f"{user_name}님이 들어왔습니다."
    if action == 'Leave':
        return f"{user_name}님이 나갔습니다."

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])