from collections import defaultdict

def solution(ings, menu, sell):
    answer = 0
    ings_dict = defaultdict(int)
    menu_benefit_dict = dict()
    
    for ings_str in ings:
        name, price = ings_str.split()
        price = int(price)
        
        ings_dict[name] = price

    for menu_str in menu:
        name, needed_ings, price = menu_str.split()
        price = int(price)
        material_cost = 0

        for needed_ing in needed_ings:
            material_cost += ings_dict[needed_ing]

        menu_benefit_dict[name] = price - material_cost
    
    for string in sell:
        name, cnt = string.split()
        cnt = int(cnt)

        answer += menu_benefit_dict[name] * cnt

    return answer


print(solution(["r 10", "a 23", "t 124", "k 9"], ["PIZZA arraak 145", "HAMBURGER tkar 180", "BREAD kkk 30", "ICECREAM rar 50", "SHAVEDICE rar 45", "JUICE rra 55", "WATER a 20"], ["BREAD 5", "ICECREAM 100", "PIZZA 7", "JUICE 10", "WATER 1"]))