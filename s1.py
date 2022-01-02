from string import ascii_uppercase

def solution(msg):
    MAX_LEN = len(msg)

    answer = []
    index_dict = {alphabet : i+1 for i, alphabet in enumerate(ascii_uppercase)} # 'ABC....XYZ'
    last_index_num = 27

    i = 0
    
    while i < MAX_LEN:
        output = 0
        next_i = i

        for j in range(i+1, MAX_LEN+1):
            cur_word = msg[i:j]

            if cur_word in index_dict:
                output = index_dict[cur_word]
                next_i = j
                if next_i == MAX_LEN:
                    answer.append(output)
            else:
                index_dict[cur_word] = last_index_num
                last_index_num += 1
                next_i = j - 1
                answer.append(output)
                break

        i = next_i
    
    return answer

print(solution('KAKA'))
print(solution('KAKAO'))
print(solution('TOBEORNOTTOBEORTOBEORNOT'))