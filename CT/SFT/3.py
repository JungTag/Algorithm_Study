import sys

def solution(n, cows, is_confirmed_list, room_len):
    result = 0
    max_range = get_max_range(n, cows)
    cur = cows[0][0]

    while cur <= room_len:
        if is_confirmed_list[cur]:
            result += 1
        cur += (max_range + 1)
    
    return result


def get_max_range(n, cows):
    max_range = float('inf')

    is_prev_cow_confirmed = False
    prev_cow_pos = -1

    for i, x in enumerate(cows):
        cow_pos, is_confirmed = x

        if (not is_confirmed and is_prev_cow_confirmed) or (is_confirmed and not is_prev_cow_confirmed):
            if i != 0:
                max_range = min(max_range, cow_pos - prev_cow_pos - 1)
        if is_confirmed:
            is_prev_cow_confirmed = True
        if not is_confirmed:
            is_prev_cow_confirmed = False
        prev_cow_pos = cow_pos

    return max_range
            

input = sys.stdin.readline
n = int(input().strip())

cows = []
room_len = float('-inf')

for _ in range(n):
    x = [int(x) for x in input().split()]
    room_len = max(room_len, x[0])
    cows.append(x)

is_confirmed_list = [0 for _ in range(room_len+1)]
for cow_num, is_confirmed in cows:
    is_confirmed_list[cow_num] = is_confirmed

print(solution(n, cows, is_confirmed_list, room_len))

    