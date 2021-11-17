# https://programmers.co.kr/learn/courses/30/lessons/85002

def solution(weights, head2head):
    answer = []
    record_list = get_record_list(weights, head2head)
    record_list.sort(key = lambda x: (-x[0], -x[1], -x[2], x[3]))
    answer = [record[3]+1 for record in record_list]

    return answer


def get_record_list(weights, head2head):
    record_list = []

    for i, i_weight in enumerate(weights):
        winning_rate = 0
        match_cnt = 0
        winning_cnt = 0
        heavy_winning_cnt = 0
        
        for j, j_weight in enumerate(weights):
            result = head2head[i][j]
            if result == 'W':
                match_cnt += 1
                winning_cnt += 1
                if i_weight < j_weight:
                    heavy_winning_cnt += 1
            if result == 'L':
                match_cnt += 1
        
        if match_cnt != 0:
            winning_rate = winning_cnt / match_cnt

        record_list.append([winning_rate, heavy_winning_cnt, i_weight, i])
        
    return record_list

print(solution([50,82,75,120], ["NLWL","WNLL","LWNW","WWLN"]))
'''
1. 승률
2. 몸무게가 무거운 복서를 이긴 횟수
3. 자기 몸무게가 무거운
4. 작은 번호
기록이 필요한 건 1+2

1) 2중 for문 돌며 1+2 기록
list = [승률(0), 횟수, 자기 몸무게, 번호]
'''