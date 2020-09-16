def solution(participant, completion):
    answer = ''
    participant_dict = {}
    for x in participant:
        if x in participant_dict.keys():
            participant_dict[x] += 1
        else:
            participant_dict[x] = 1
    for x in completion:
        participant_dict[x] -= 1
    for key, value in participant_dict.items():
        if value != 0:
            answer = key
            return answer

# solution(["leo", "kiki", "eden"], ["eden", "kiki"])