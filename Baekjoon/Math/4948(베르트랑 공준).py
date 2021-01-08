N = 123456
max_num = 0
isPrime = [False, False] + [True]*(2*N - 1)

def count_num(n):
    global max_num
    if max_num < n:
        for i in range(max_num*2 + 1, 2*n + 1): # max_num*2까지는 계산이 되었으므로
            if isPrime[i]:
                for j in range(2*i, 2*N + 1, i):
                    isPrime[j] = False
        max_num = n
        return isPrime[n+1:2*n + 1].count(True)
    else:
        return isPrime[n+1:2*n + 1].count(True)


while True:
    n = int(input())
    if n:
        print(count_num(n))
    else:
        break

'''
N = 123456
max_num = 0
isPrime = [False, False] + [True]*(2*N - 1)

for i in range(2, 2*N + 1): # max_num*2까지는 계산이 되었으므로
    if isPrime[i]:
        for j in range(2*i, 2*N + 1, i):
            isPrime[j] = False

while True:
    n = int(input())
    if n:
        print(isPrime[n+1:2*n + 1].count(True))
    else:
        break
'''    
'''
에라토스테네스의 체 이용
n=1000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
print(primes)
'''