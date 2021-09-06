def solution(prices):
    answer = 0
    mins, maxs = get_candis(prices)
    answer = get_answer(mins, maxs)
    return answer

def get_candis(org_prices):
    prices = org_prices[:]
    mins, maxs = [], []
    min_idxs = []
    max_idxs = []
    for _ in range(2):
        min_v, min_idx = float('inf'), 0
        max_v, max_idx = float('-inf'), 0
        for i, v in enumerate(prices):
            if v < min_v and i not in min_idxs:
                min_v, min_idx = v, i
            if v > max_v and i not in max_idxs:
                max_v, max_idx = v, i
        mins.append([min_v, min_idx])
        maxs.append([max_v, max_idx])
        min_idxs.append(min_idx)
        max_idxs.append(max_idx)
    return mins, maxs

def get_answer(mins, maxs):
    candis = []
    pairs = [[0, 0], [0, 1], [1, 0], [1, 1]]
    for x, y in pairs:
        if mins[x][1] < maxs[y][1]:
            candis.append(maxs[y][0] - mins[x][0])
        else:
            candis.append(0)
    return max(candis[0]+candis[3], candis[1]+candis[2])

x = [[1, 2, 3, 4], [1, 2, 4, 1, 2, 3], [4, 3, 2, 1, 4],[4,3,2,1],[1, 10, 5, 11, 7]]
for prices in x:
    print(solution(prices))