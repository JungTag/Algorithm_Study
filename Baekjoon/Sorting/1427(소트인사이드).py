def merge_sort(A, first, last):
    if first >= last: return
    m = (first + last) // 2
    merge_sort(A, first, m)
    merge_sort(A, m + 1, last)
    merge_two_list(A, first, last)

def merge_two_list(A, first, last):
    m = (first + last) // 2
    i, j = first, m + 1
    B = []
    while i <= m and j <= last:
        if A[i] > A[j]:
            B.append(A[i])
            i += 1
        else:
            B.append(A[j])
            j += 1
    for k in range(i, m + 1):
        B.append(A[k])
    for k in range(j, last + 1): # m+1이 아니라 꼭 j부터 시작해야함!!
        B.append(A[k])
    for i in range(first, last + 1):
        A[i] = B[i - first]
        
    
n = input()
N = []
my_str = ""
for i in range(len(n)):
    N.append(int(n[i]))
merge_sort(N, 0, len(N) - 1)
for number in N:
    my_str += str(number)
print(int(my_str))
    


