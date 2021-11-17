# https://programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    answer = -1

    for i in range(1, count+1):
        money -= price * i
    
    if money < 0:
        answer = -(money)
    else:
        answer = 0

    return answer

print(solution(3, 20, 1))