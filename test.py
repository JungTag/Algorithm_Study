num = int(input())
answer = 0
x = []

for i in range(1, num):
    x = map(int, str(i))
    y =i + sum(x)

    if y==num:
        answer = i
        break

print(answer)