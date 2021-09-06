from itertools import combinations
def solution(numbers, target):
    answer = 0; plus_index_list = []
    for i in range(1, len(numbers)+1):
        plus_index_list += list(combinations(range(len(numbers)), i))
    for plus_index in plus_index_list:
        sum = 0
        for i in range(len(numbers)):
            sum += [-numbers[i], numbers[i]][i in plus_index]
        answer += [0, 1][sum == target]
    return answer

numbers = [1,1,1,1,1]
target = 3
print(solution(numbers, target))
# x = 3
# print(["one", "zero"][x == 3]) -> 참이면 두 번째 원소
'''
index로 접근하는 것이 훨씬 빠르다 항상 명심!!
combinations보다 더 좋은 방법이 있지 않을까?
'''