def solution(numbers):
    answer = ''
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])
    numbers.sort(reverse = True)
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if int(numbers[i]+numbers[j]) < int(numbers[j]+numbers[i]):
                temp = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = temp
    for number in numbers:
        answer += number
    answer = str(int(answer))
    return answer

# numbers = [40, 403]
# numbers = [10, 101]
# numbers = [1, 11, 111, 1111]
# numbers = [0,0,0,0,0,0]

# numbers = [500, 11, 12, 13] 
# 500131211
# numbers = [2, 20, 220]
#222020
# numbers = [6, 646] 
#6646
# numbers = [0, 0, 0, 0] 
#0
# numbers = [10,101] 
#10110
# numbers = [0, 0, 70] 
#7000
# numbers = [2357, 235785] 
#2357852357
# numbers = [3, 30, 31, 33] 
# 3333130
# numbers = [1,112]
# numbers = [1,2,21, 21]
numbers = [12, 121]
numbers = [21, 212]
print(solution(numbers))
# test = [[[6, 10, 2], "6210"],
#   [[3, 30, 34, 5, 9], "9534330"],
#   [[10, 101], '10110'],
#   [[1, 11, 111, 1111], '1111111111'],
#   [[0, 0, 0, 0, 0, 0], '0'],
#   [[2,20,200], '220200'],
#   [[0,0,70], '7000'],
#   [[0,0,0,1000], '1000000'],
#   [[0,0,1000,0], '1000000'],
#   [[1000,0,0], '100000'],
#   [[12,121], '12121'],
#   [[21,212], '21221'],
#   [[11, 12, 10], '121110'],
#   [[0,0,0,1], '1000'],
#   [[1,2,3,1,1,3], '332111'],
#   [[1,2,21, 21], '221211']
# ]
# for x in test:
#     case, result = x
#     print(f"? {solution(case)} == {result}")
    