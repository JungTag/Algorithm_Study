from collections import deque

def solution(n, results):
    answer = 0
    W, L= [set() for _ in range(n+1)], [set() for _ in range(n+1)]
    
    for i in range(1, n+1):
        for result in results:
            winner, loser = result[0], result[1]
            if i == winner:
                W[i].add(loser)
            if i == loser:
                L[i].add(winner)
        for winner in L[i]: # i를 이긴 사람은 i가 이긴 사람들을 다 이길 수 있다.
            W[winner].update(W[i])
        for loser in W[i]: # i에게 진 사람은 i를 이긴 사람들을 못이긴다.
            L[loser].update(L[i])
                
    for i in range(1, n+1):
        if len(W[i]) + len(L[i]) == n - 1:
            answer += 1
            
    return answer
'''
from collections import deque

def solution(n, results):
    answer = 0
    G = {i:[] for i in range(1, n+1)}
    P, C= [set() for _ in range(n+1)], [set() for _ in range(n+1)]
    for w, v in results:
        G[v].append(w)
        P[w].add(v)
        
    
    starts = []
    for i in range(1, n+1):
        if not P[i] and i != 0:
            starts.append(i)
    
    Q = deque([])
    for start in starts:
        Q.append(start)

    while Q:
        v = Q.popleft()
        for u in G[v]:
            Q.append(u)
            P[u].update(P[v])
            C[v].add(u)
            for parent in P[v]:
                C[parent].update(C[v])
    
    for i in range(1, n+1):
        if len(P[i]) + len(C[i]) == n - 1:
            answer += 1
    print(P)
    print(C)
    print(answer)    
    return answer
'''
'''
def solution(n, results):
    answer = 0
    G = {i:[] for i in range(1, n+1)}
    P, W, L = [set() for _ in range(n+1)], [0 for _ in range(n+1)], [0 for _ in range(n+1)]

    for w, v in results:
        G[v].append(w)
        P[w].add(v)
    
    starts = []
    for i in range(1, n+1):
        if not P[i] and i != 0:
            starts.append(i)
    
    Q = deque([])
    for start in starts:
        Q.append([start, 0])

    while Q:
        v, d = Q.popleft()
        for parent in P[v]:
            L[parent] += 1
        W[v]= d
        for u in G[v]:
            Q.append([u, d+1])
            P[u].update(P[v])
    
    matchs = list(zip(W, L))
    print(P)
    print(matchs)
    for match in matchs:
        if match[0] + match[1] == n - 1:
            answer += 1

    print(answer)
    return answer
'''
solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])

n = 5
results = [[3, 5], [4, 2], [4, 5], [5, 1], [5, 2]]
solution(n, results)