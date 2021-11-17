# https://programmers.co.kr/learn/courses/30/lessons/17687

def solution(n, t, m, p):
    answer = ''
    total_converted_num = ''
    total_len = 0
    num = 0

    while t * m > total_len:
        converted_num = convert_to_n(num, n)
        total_converted_num += converted_num
        total_len += len(converted_num)
        num += 1
    
    for i in range(t):
        idx = (p-1) + m*i
        answer += total_converted_num[idx]
        
    return answer


def convert_to_n(decimal, n):
    hex_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    base = ''

    if decimal == 0:
        return '0'

    while decimal > 0:
        decimal, mod = divmod(decimal, n)
        if mod >= 10:
            mod = hex_dict[mod]
        base += str(mod)
    
    return base[::-1]


# print(solution(10, 10, 2, 1))
print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))