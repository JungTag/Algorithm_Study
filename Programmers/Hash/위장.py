def solution(clothes):
    clothes_dict = {}
    answer = 0
    for name, kind in clothes:
        if kind in clothes_dict.keys():
            clothes_dict[kind] += 1
        else:
            clothes_dict[kind] = 1
    all_cloth_list = list(clothes_dict.values())
    if len(all_cloth_list) != 1:
        temp = 1
        for x in all_cloth_list:
            temp *= (x+1)
        answer += (temp-1)
    else:
        answer = all_cloth_list[0]
    return answer
    
'''
from itertools import product
from itertools import combinations

def solution(clothes):
    clothes_dict = {}
    answer = 0
    for name, kind in clothes:
        if kind in clothes_dict.keys():
            clothes_dict[kind] += 1
        else:
            clothes_dict[kind] = 1

    all_cloth_list = list(clothes_dict.values())
    prod_all = 1
    if len(all_cloth_list) != 1:
        for i in range(2, len(all_cloth_list)):
            combi = list(combinations(all_cloth_list, i))
            for x in combi:
                temp = 1
                for y in x:
                    temp *= y
                answer += temp
        for x in all_cloth_list: # i = 5
            prod_all *= x
            answer += x
        answer += prod_all
    else:
        answer = all_cloth_list[0]
    return answer
'''