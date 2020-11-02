def solution(people, limit):
    people.sort(); answer = 0; cnt = 0
    left_index = 0; right_index = len(people) - 1
    while True:
        if left_index == right_index:
            answer += 1
            break
        if left_index > right_index:
            break
        if people[left_index] + people[right_index] <= limit:
            left_index += 1; right_index -= 1; answer += 1
        else:
            right_index -= 1; answer += 1
    return answer

people = [70, 50, 80, 50]; limit = 100
print(solution(people, limit))