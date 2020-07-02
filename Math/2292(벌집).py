from sys import stdin
num = int(stdin.readline())

if num == 1:
    print(1)
else:
    num -= 1
    x = 2
    while num - 6*x + 6 > 0:
        num = num - 6*x + 6
        x += 1
    print(x)
