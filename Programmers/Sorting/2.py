def solution(numbers):
    answer = ''
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])
    numbers.sort(reverse =True)
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if len(numbers[i]) == len(numbers[j]) or numbers[i][0] != numbers[j][0]: 
                break
            else:
                len_diff = len(numbers[i]) - len(numbers[j])
                if numbers[i][len_diff] < numbers[j][0]:
                    temp = numbers[i]
                    numbers[i] = numbers[j] 
                    numbers[j] = temp
    for number in numbers:
        answer += number
    return answer