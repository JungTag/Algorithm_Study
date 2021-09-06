import sys, itertools

def simulate(pm):
    hit_idx, score = 0, 0

    for inning in range(n):
        cnt = 0
        b1, b2, b3 = 0, 0, 0
        while cnt < 3:
            if results[inning][pm[hit_idx]] == 0:
                cnt += 1
            elif results[inning][pm[hit_idx]] == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif results[inning][pm[hit_idx]] == 2:
                score += (b2 + b3)
                b1, b2, b3 = 0, 1, b1
            elif results[inning][pm[hit_idx]] == 3:
                score += (b1 + b2 + b3)
                b1, b2, b3 = 0, 0, 1
            else:
                score += 1 + (b1 + b2 + b3)
                b1, b2, b3 = 0, 0, 0
            hit_idx = (hit_idx+1) % 9
    
    return score

n = int(sys.stdin.readline().strip())
results = [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)]
pms = list(itertools.permutations([i for i in range(9) if i != 0], 8))
max_score = 0

for pm in pms:
    pm = list(pm[:3])+[0]+list(pm[3:])
    score = simulate(pm)
    max_score = max(max_score, score)
    
print(max_score)

''' 테케 6번 안됨... + 리스트 쓰면 시간 초과
def simulate(pm):
    inning, hit_idx, cnt, total_score = 0, 0, 0, 0
    q = [0]*4

    while inning < n: # 0이닝부터 n-1이닝까지
        if cnt >= 3:
            inning += 1
            cnt = 0
            q = [0]*4
            continue
        result = results[inning][pm[hit_idx]]
        hit_idx = (hit_idx+1) % 9
        if result == 0:
            cnt += 1
        else:
            q, score = advance(q, result)
            total_score += score

    return total_score


def advance(q, result):
    score = 0
    nq = [0]*4

    for i in range(3):
        if q[i]:
            ni = i+result
            if ni >= 3:
                nq[i] = 0
                score += 1
            else:
                nq[ni] = 1
    if result < 4:
        nq[result-1] = 1
    else:
        score += 1

    return nq, score


n = int(sys.stdin.readline().strip())
results = [[int(x) for x in sys.stdin.readline().split()] for _ in range(n)]
pms = list(itertools.permutations([i for i in range(9) if i != 0], 8))
max_score = 0

for pm in pms:
    pm = list(pm)
    pm.insert(3,0)
    score = simulate(pm)
    max_score = max(max_score, score)
    
print(max_score)
'''