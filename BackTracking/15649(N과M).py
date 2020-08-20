import sys
n, m = map(int, sys.stdin.readline().split())
START_LENGTH = 1
num_list = [i for i in range(1, n+1)]

def back_track(length, num, candidate_list, sequence):
    if length >= m: 
        sequence += str(num)
        print(sequence.rstrip())
        return
    sequence += (str(num) + " ")
    for next_num in candidate_list:
        new_num_list = candidate_list[:]
        new_num_list.remove(next_num)
        back_track(length+1, next_num, new_num_list, sequence)
    
for num in range(1, n+1):
    new_num_list = num_list[:]
    new_num_list.remove(num)
    back_track(
        START_LENGTH, num,
        new_num_list, "")

'''
처음엔 리스트로 했는데 출력할 때 귀찮아서 그냥 문자열로 처리했다.
def back_track(length, num, candidate_list, sequence):
    if length >= k:
        sequence.append(num)
        output(sequence)  # pseudo code
        return
    sequence.append(num)
    for next_num in candidate_list:
        new_sequence = sequence[:]
        new_num_list = candidate_list[:]
        new_num_list.remove(next_num)
        back_track(length+1, next_num, new_num_list, new_sequence)
    
for num in range(1, n+1):
    new_num_list = num_list[:]
    new_num_list.remove(num)
    back_track(
        START_LENGTH, num,
        new_num_list, [])
'''