T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    back_num = ((N-1) // H) + 1
    front_num = ((N-1) % H) + 1
    F = str(front_num)
    B = str(back_num)
    if back_num < 10: B = '0' + B
    print(F + B)
