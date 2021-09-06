n = int(input())
my_list = []
const_list=[]
a = b = c = d = e = f = 0

for i in range(1,55): #자릿수의 합은 최소 1부터~ 최대 55(999999)까지
    my_list.append(n - i) #입력받은 수에서 모든 경우의 수를 빼준 후 배열에 넣어준다.

for m in my_list: 
    a = m // 100000
    b = (m % 100000) // 10000
    c = (m % 10000) // 1000
    d = (m % 1000) // 100
    e = (m % 100) // 10
    f = m % 10 
    sum = a+ b + c + d + e + f
    if n == m + sum: const_list.append(m)

const_list.sort()

if const_list:
    print(const_list[0])
else:
    print(0)