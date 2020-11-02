def solution(numbers):
    numbers = list(map(str,numbers))
    numbers.sort(key = lambda x : x*4, reverse=True)
    print(numbers)
    answer= str(int(''.join(numbers)))
    return answer