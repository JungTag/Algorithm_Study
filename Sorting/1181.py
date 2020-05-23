import sys

n = int(input())
A = ""
for i in range(n):  #.append의 형식으로 입력받으면 2차원 리스트가 됨
    A += sys.stdin.readline()
li = A.split()

li = list(set(li))  #중복제거


def merge_sort(li, first, last):
    if first >= last: return
    m = (first + last) // 2
    merge_sort(li, first, m)
    merge_sort(li, m + 1, last)
    unite_twoList(li, first, last)

def unite_twoList(li, first, last):
    m = (first + last) // 2
    i, j = first, m + 1
    U = []
    while i <= m and j <= last:
        if len(li[i]) == len(li[j]):
            if li[i] > li[j]:
                U.append(li[j])
                j += 1
            else:
                U.append(li[i])
                i += 1
        elif len(li[i]) > len(li[j]):
            U.append(li[j])
            j += 1
        else:
            U.append(li[i])
            i += 1
    for x in range(i, m + 1):
        U.append(li[x])
    for x in range(j, last + 1):
        U.append(li[x])
    for i in range(first, last + 1):
        li[i] = U[i - first]

merge_sort(li, 0, len(li)-1)
for x in li:
    print(x)

    

