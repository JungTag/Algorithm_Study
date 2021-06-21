def solution(grades, weights, threshold):
    answer = -1234567890; sum_mul = 0
    grade_dict = {"A+": 10, "A0": 9, "B+": 8, "B0": 7, "C+": 6, "C0": 5, "D+": 4, "D0": 3, "F": 0}
    for i in range(len(grades)):
        mul = grade_dict[grades[i]] * weights[i]
        sum_mul += mul
    answer = sum_mul - threshold
    return answer
grades = ["A+","D+","F","C0"]; weights = [2,5,10,3]; threshold = 50
print(solution(grades, weights, threshold))