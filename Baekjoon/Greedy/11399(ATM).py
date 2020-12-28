# 1 = 1 <- min_time
# 1 + 2 = 3
# 1 + 2 + 3 = 6 
# 1 + 2 + 3 + 3 = 9
# 1 + 2 + 3 + 3 + 4 = 13

N = int(input())
P = [int(x) for x in input().strip().split()]
P.sort() 
min_list = []

for i in range(len(P)):
    min_time = 0
    for j in range(0, i+1):
        min_time += P[j]
    min_list.append(min_time)

print(sum(min_list))