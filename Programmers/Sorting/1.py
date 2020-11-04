def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command[0], command[1], command[2]
        sliced_array = array[i-1:j].sorted()
        answer.append(sliced_array[k-1])
    return answer