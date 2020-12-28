n = int(input())

def Fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        first, last = 0, 1
        for i in range(n-1):
            first, last = last, first+last
        return last

print(Fibo(n))
    
        
        

