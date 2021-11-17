# https://programmers.co.kr/learn/courses/30/lessons/77486

def solution(enroll, referral, seller, amount):
    PRICE_OF_TOOTHBRUSH = 100
    ANCESTOR_PROFIT_RATIO = 0.1

    answer = []
    parent_dict = dict(zip(enroll, referral))
    profit_dict = {key: 0 for key in enroll}
    
    for i, sell_amount in enumerate(amount):
        current = seller[i]
        parent = parent_dict[current]

        total_profit = sell_amount * PRICE_OF_TOOTHBRUSH 
        ancestor_profit = int(total_profit * ANCESTOR_PROFIT_RATIO)
        own_profit = total_profit - ancestor_profit

        profit_dict[current] += own_profit

        while parent != "-" and ancestor_profit >= 1:
            total_profit = ancestor_profit
            ancestor_profit = int(total_profit * ANCESTOR_PROFIT_RATIO)
            own_profit = total_profit - ancestor_profit
            
            current, parent = parent_dict[current], parent_dict[parent]
            
            profit_dict[current] += own_profit
    
    answer = list(profit_dict.values())

    return answer

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))

'''
john: []
mary: []
edward : mary
emily: mary

sam : edward

parent_dict = {}
profit_dict = {}
1. enroll + referral -> parent_dict
2. amount 순회하며 parent타고 올라가서 계산
- 원 단위 절사
- 1원 미만인 경우는 모두 가져감

단, 10% 를 계산할 때에는 원 단위에서 절사하며, 10%를 계산한 금액이 1 원 미만인 경우에는 이득을 분배하지 않고 자신이 모두 가집니다.
'''