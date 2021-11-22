import sys
sys.setrecursionlimit(10**9)

def solution(time, gold, upgrade):
    global TIME, GOLD, UPGRADE, answer, MAX_UPGRADE_INDEX
    TIME, GOLD, UPGRADE, answer, MAX_UPGRADE_INDEX = time, gold, upgrade, 0, len(upgrade)-1

    dfs(0, 0, 0)

    return answer

def dfs(cur_time, cur_gold, cur_upgrade_index):
    global TIME, GOLD, UPGRADE, answer, MAX_UPGRADE_INDEX

    needed_time = UPGRADE[cur_upgrade_index][1]

    if cur_time >= TIME or cur_time + needed_time > TIME:
        answer = max(answer, cur_gold)
        return

    if cur_upgrade_index + 1 <= MAX_UPGRADE_INDEX:
        next_upgrade_index = cur_upgrade_index + 1
        next_needed_upgrade_gold = UPGRADE[next_upgrade_index][0]
        if cur_gold >= next_needed_upgrade_gold:
            dfs(cur_time, cur_gold - next_needed_upgrade_gold, next_upgrade_index)

    dfs(cur_time+needed_time, cur_gold+GOLD, cur_upgrade_index)

# print(solution(100, 200, [[0, 5], [1500, 3], [3000, 1]]))
print(solution(11, 1000, [[0, 5], [100, 4], [200, 3]]))