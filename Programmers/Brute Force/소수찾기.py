from itertools import permutations

def solution(numbers):
    answer = 0; checked_num = set()
    for i in range(1, len(numbers)+1):
        combi = list(map(''.join, permutations(numbers, i)))
        combi = list(set(combi))
        for x in combi:
            x = int(x)
            if x not in checked_num:
                if is_prime(x):
                    answer += 1
                checked_num.add(x)
    return answer

def is_prime(n: int) -> bool: 
    if n < 2: 
        return False 
    if n in (2, 3): 
        return True 
    if n % 2 == 0 or n % 3 == 0: 
        return False 
    if n < 9: 
        return True
    k, l = 5, n**0.5
    while k <= l: 
        if n % k == 0 or n % (k+2) == 0: 
            return False 
        k += 6 
    return True