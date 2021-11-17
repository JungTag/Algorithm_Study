from collections import defaultdict

def solution(gems):
    answer = [0, 0]
    gems_set = set(gems)
    gems_dict = defaultdict(int)

    LEN_OF_GEMS = len(gems)
    LEN_OF_GEMS_SET = len(gems_set)

    start = end = 0
    diff = float('inf')

    while end < LEN_OF_GEMS:
        gems_dict[gems[end]] += 1
        end += 1

        if len(gems_dict) >= LEN_OF_GEMS_SET:
            while start < end:
                if gems_dict[gems[start]] > 1:
                    gems_dict[gems[start]] -= 1
                    if gems_dict[gems[start]] == 0:
                        del gems_dict[gems[start]]
                    start += 1
                elif get_diff(start, end) < diff:
                    answer[0], answer[1] = start+1, end
                    diff = get_diff(start, end)
                    break
                else:
                    break
        
    return answer

def get_diff(start, end):
    return end - start

print(solution(["A","A","A","B","B"])) # [3,4]
print(solution(["A"]))  # [1,1]
print(solution(["A","B","B","B","B","B","B","C","B","A"])) # [8,10]
print(solution(["A", "B", "C", "B", "F", "D", "A", "F", "B", "D", "B"])) # [3,7]

'''
@ 조건: O(nlogn)
gems -> set

1. for문 돌면서 gems_set 만듦, 이때 집합의 원소 개수 기록
2. 뒤에서부터 for문 돌면서 원소 개수 == len(gems_set)인 최소 인덱스(end) 구함
3. end부터 set하나 만들고 cnt 기록해두면서 체크!!
4. cnt == len(gems_set)인 인덱스(start) 구함

'''