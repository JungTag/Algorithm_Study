from collections import deque

def solution(people, limit):
    people = deque(sorted(people)); answer = 0; cnt = 0
    while people:
        if people[0] + people[1] > limit:
            answer += len(people)
            break
        for i in range(len(people)-1, -1, -1):
            if len(people) == 1:
                answer += 1
                break
            if people[0] + people[i] <= limit:
                people.popleft(); del people[i-1]; answer += 1
    return answer

people = [70, 50, 80, 50]; limit = 100
print(solution(people, limit))