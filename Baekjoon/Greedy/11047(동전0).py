import sys
N, K = map(int, input().split())
coin_list = [sys.stdin.readline().strip() for i in range(N)]
coin_list = list(map(int, coin_list))
min = 0
coin_list.reverse()

for coin in coin_list:
    if coin <= K:
        cnt = K // coin
        K = K % (cnt * coin)
        min += cnt

print(min)


