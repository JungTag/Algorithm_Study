def solution(number, k):
    answer = ''
    left_index = 0; right_index = k+1; max_index = 0
    for _ in range(len(number) - k):
        max_num = "0"
        for i in range(left_index, right_index):  # 최대값이 9이면 탐색을 멈춘다
            if max_num < number[i]:
                max_num = number[i]
                if max_num == "9": 
                    max_index = i
                    break
        if max_num != "9":
            for i in range(left_index, right_index):
                if number[i] == max_num:
                    max_index = i
                    break
        left_index = max_index + 1; right_index += 1
        answer += max_num    
    return answer
'''
def solution(number, k):
    answer = ''
    left_index = 0; right_index = k+1; max_index = 0; max_num = 0
    for _ in range(len(number) - k):
        max_num = max(number[left_index:right_index])
        for i in range(left_index, right_index):
            if number[i] == max_num:
                max_index = i
                break
        left_index = max_index + 1; right_index += 1
        answer += max_num
    return answer
'''
'''
import operator

def solution(number, k):
    answer = ''
    left_index = 0; right_index = k+1; max_index = 0; max_num = 0
    for _ in range(len(number) - k):
        max_num = max(number[left_index:right_index])
        max_index_list = [index for index, value in enumerate(number) if value == max_num]
        for i in max_index_list:
            if i >= left_index:
                max_index = i
                break
        left_index = max_index + 1; right_index += 1
        answer += max_num
        
    return answer
'''