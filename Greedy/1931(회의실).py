import sys

def merge_sort(A, first, last):
    if first >= last: return
    merge_sort(A, first, (first + last)//2)
    merge_sort(A, (first + last)//2 + 1, last)
    merge_two_lists(A, first, last)

def merge_two_lists(A, first, last):
    m = (first + last)//2
    i, j = first, m+1
    B = [] # 두 리스트를 병합하여 담을 리스트
    while i <= m and j <= last: # 한 리스트가 모두 B에 담길 때까지 반복
        if A[i][1] < A[j][1]: 
            B.append(A[i])
            i += 1
        elif A[i][1] > A[j][1]: 
            B.append(A[j])
            j += 1
        else:
            if A[i][0] < A[j][0]:
                B.append(A[i])
                i += 1
            else:
                B.append(A[j])
                j += 1
    # 두 개의 반복문 중 하나만 작동
    for k in range(i, m+1):
        B.append(A[k])
    for k in range(j, last+1): # m+1이 아니라 꼭 j부터 시작해야함!!
        B.append(A[k])
    for i in range(first, last+1): #copy list
        A[i] = B[i-first]

N = int(input())
input_list = [sys.stdin.readline().strip() for i in range(N)]
con_list = []
start = []
finish = []

for x in input_list:
    con_list.append(list(map(int, x.split())))
merge_sort(con_list, 0, len(con_list) - 1)

for x, y in con_list:
    start.append(x)
    finish.append(y)

C = [0]
k = 0

for i in range(1, N):
    if finish[k] <= start[i]:
        C.append(i)
        k = i
        
print(len(C))