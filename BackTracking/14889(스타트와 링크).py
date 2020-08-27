import sys
from itertools import combinations

def make_combi():
    num_list = [i for i in range(n)]
    combi_list = list(combinations(num_list, n//2))
    for i in range(len(combi_list)//2):
        combi_pair_list.append([combi_list[i*2], combi_list[-1-(i*2)]])

def calculate_ability(combi_list1, combi_list2):
    sum1, sum2 = 0, 0
    combi_list1 = list(combinations(combi_list1, 2))
    combi_list2 = list(combinations(combi_list2, 2))
    for pair in combi_list1:
        i, j = pair[0], pair[1]
        sum1 += (ability[i][j] + ability[j][i])
    for pair in combi_list2:
        i, j = pair[0], pair[1]
        sum2 += (ability[i][j] + ability[j][i])
    return abs(sum1 - sum2)
    
n = int(sys.stdin.readline().strip())
ability = []
for _ in range(n):
    ability.append([int(x) for x in sys.stdin.readline().split()])
combi_pair_list = []
make_combi()
min_val = float('inf')

for x,y in combi_pair_list:
    cur_val = calculate_ability(x,y)
    if cur_val < min_val:
        min_val = cur_val
print(min_val)