import sys

n = int(input())
input_list = [sys.stdin.readline() for i in range(n)]
li = []
for x in input_list:
    li.append(list(map(str, x.split())))
for i in range(len(li)):
    li[i][0] = int(li[i][0])

def merge_sort(A, first, last):
    if first >= last: return
    m = (first+last)//2
    merge_sort(A, first, m)
    merge_sort(A, m+1, last)
    unite_list(A, first, last)

def unite_list(A, first, last):
    m = (first+last)//2
    i, j = first, m+1
    B = []
    while i <= m and j <= last:
        if A[i][0] <= A[j][0]: 
            B.append(A[i]) #여기가 포인트! age가 같으면 먼저 입력된 데이터부터 append해준다.
            i += 1
        else:
            B.append(A[j])
            j += 1
    for k in range(i, m+1):
        B.append(A[k])
    for k in range(j, last+1):
        B.append(A[k])
    for i in range(first, last+1):
        A[i] = B[i-first]

merge_sort(li, 0, len(li)-1)
for x, y in li:
    print(x, y)

