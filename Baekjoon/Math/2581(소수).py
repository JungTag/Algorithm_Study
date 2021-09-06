M = int(input())
N = int(input())
p = []
sum = 0

def checkPrime(num):
    global sum
    if num % 2 == 0:
        if num == 2:
            sum += num
            p.append(num)
    else:
        if num > 1:
            for n in range(2, num):
               if num % n == 0: return
            sum += num
            p.append(num)

for i in range(M, N+1):
    checkPrime(i)

if sum != 0:
    print(sum)
    print(p[0])
else:
    print(-1)

            
    

