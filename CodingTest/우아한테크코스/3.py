def solution(money, expected, actual):
    answer = -1; bet = 100
    for i in range(len(expected)):
        if expected[i] == actual[i]:
            money += bet
            bet = 100
        else:
            money -= bet
            if money - (bet * 2) < 0:
                bet = money
            else:
                bet *= 2
    answer = money
    return answer