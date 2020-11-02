from collections import deque

def solution(people, limit):
    people = deque(sorted(people)); answer = 0; cnt = 0
    while people:
        sum = 0
        for i in range(len(people)):
            sum += people[i]; cnt += 1
            if sum > limit or cnt > 2:
                for _ in range(i): people.popleft()
                cnt = 0
                break
            if len(people) == 1:
                people.popleft()
                break
        answer += 1
        print(people, answer)
    return answer

people = [40, 40, 40]; limit = 100
solution(people, limit)