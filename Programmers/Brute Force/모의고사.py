def solution(answers):
    arr1, arr2, arr3 = [1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]
    cnt1, cnt2, cnt3 = 0, 0, 0
    answer1, answer2, answer3 = [], [], []
    
    for _ in range((len(answers)//len(arr1))+1):
        answer1.extend(arr1)
    for _ in range((len(answers)//len(arr2))+1):
        answer2.extend(arr2)
    for _ in range((len(answers)//len(arr3))+1):
        answer3.extend(arr3)
        
    for i in range(len(answers)):
        answer = answers[i]
        if answer == answer1[i]:
            cnt1 += 1
        if answer == answer2[i]:
            cnt2 += 1
        if answer == answer3[i]:
            cnt3 += 1
            
    hs = max(cnt1, cnt2, cnt3)
    answer = []
    if hs == cnt1:
        answer.append(1)
    if hs == cnt2:
        answer.append(2)
    if hs == cnt3:
        answer.append(3)
    return answer