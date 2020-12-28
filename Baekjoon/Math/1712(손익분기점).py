a, b, c = map(int, input().split())
if b >= c:
    print(-1)
else:
    num = (a // (c - b)) + 1
    print(num)

# b==c일 경우에 런타임 에러 발생
