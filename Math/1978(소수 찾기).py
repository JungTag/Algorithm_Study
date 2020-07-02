T = int(input())
a = [int(x) for x in input().strip().split()]
cnt = 0
for i in range(T):
    if a[i] % 2 == 0:
        if a[i] == 2: cnt += 1
    else:
        if a[i] > 1:
            for n in range(2, a[i]):
               if a[i] % n == 0:
                   cnt -= 1
                   break
            cnt += 1
print(cnt)
            
    

