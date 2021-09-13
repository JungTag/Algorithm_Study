def solution(lottos, win_nums):
    answer = []
    cnt = 0
    c_cnt = 0
    win_nums_set = set(win_nums)
    for lotto in lottos:
        if lotto == 0:
            cnt += 1
        elif lotto in win_nums_set:
            c_cnt += 1
    answer = [get_grade(c_cnt + cnt), get_grade(c_cnt)]        
    return answer

def get_grade(cnt):
    if cnt == 6:
        return 1
    elif cnt == 5:
        return 2
    elif cnt == 4:
        return 3
    elif cnt == 3:
        return 4
    elif cnt == 2:
        return 5
    else:
        return 6