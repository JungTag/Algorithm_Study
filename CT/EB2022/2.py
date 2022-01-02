import sys
sys.setrecursionlimit(10**6)


def solution(stones, k):
    answer = ''
    answer_set = set()
    visited = set()

    dfs(answer_set, visited, '', stones, k)

    if len(answer_set) < 1:
        return '-1'
    
    answer = sorted(list(answer_set))[-1]

    return answer


def dfs(answer_set, visited, current_node, stones, k):
    visited.add(current_node)

    if is_satisfied(stones, k):
        answer_set.add(current_node)
        return

    for i in range(len(stones)):
        next_node = current_node + str(i)

        if (next_node not in visited) and is_possible(stones, i):
            pick_stone(stones, i)
            dfs(answer_set, visited, next_node, stones, k)
            restore_stones(stones, i)


def is_satisfied(stones, k):
    LEN_OF_STONES = len(stones)

    k_cnt = 0
    zero_cnt = 0

    for stone in stones:
        if stone == k:
            k_cnt += 1
        if stone == 0:
            zero_cnt += 1
    
    if k_cnt == 1:
        if k_cnt + zero_cnt == LEN_OF_STONES:
            return True
    
    return False


def is_possible(stones, index):
    for i, stone in enumerate(stones):
        if i == index:
            continue
        if stone == 0:
            return False
    return True


def pick_stone(stones, index):
    for i in range(len(stones)):
        if i == index:
            stones[i] += 1
        else:
            stones[i] -= 1


def restore_stones(stones, index):
    for i in range(len(stones)):
        if i == index:
            stones[i] -= 1
        else:
            stones[i] += 1


# print(solution([1, 3, 2], 3))
print(solution([4, 2, 2, 1, 4], 1))