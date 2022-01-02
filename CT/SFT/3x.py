import sys

def solution(n, cow_list, is_confirmed_list, room_len, confirmed_cnt):
    result = confirmed_cnt
    left, right = 1, room_len

    while left <= right:
        mid = (left + right) // 2
        if is_possible(mid):
            left = right + 1
            # do
        else:
            right = left - 1


def is_possible(r, cow_list, is_confirmed_list, confirmed_cnt):
    total = 0
    for cow_num, is_confirmed in cow_list:
        pass

input = sys.stdin.readline
n = int(input().strip())
cow_list = [[int(x) for x in input().split()] for _ in range(n)]

cow_list2 = []
room_len = float('-inf')
confirmed_cnt = 0

for _ in range(n):
    x = input().split()
    room_len = max(room_len, int(x[0]))
    cow_list2.append([map(int, x)])

# is_confirmed_list = [0 for _ in range(room_len+1)]
# for cow_num, is_confirmed in cow_list2:
#     if is_confirmed:
#         confirmed_cnt += 1
#     is_confirmed_list[cow_num] = is_confirmed
    