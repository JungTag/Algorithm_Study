def solution(n, k, bulbs):
    answer = 0
    bulbs = list(bulbs)

    for i in range(n):
        bulb = bulbs[i]

        if bulb == 'R':
            continue
        if i+k > n:
            return -1
        else:
            while bulbs[i] != 'R':
                convert_bulbs(i, i+k-1, bulbs)
                answer += 1

    return answer


def convert_bulbs(start, end, bulbs):
    new_bulbs = []

    for i in range(start, end+1):
        bulb = bulbs[i]

        if bulb == 'R':
            new_bulbs.append('G')
        elif bulb == 'G':
            new_bulbs.append('B')
        else:
            new_bulbs.append('R')

    bulbs[start:end+1] = new_bulbs

print(solution(6, 3, "RBGRGB"))