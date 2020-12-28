import sys

n = int(input())
A = ""
for i in range(n):  #.append의 형식으로 입력받으면 2차원 리스트가 됨
    A += sys.stdin.readline()
li = A.split()

li = list(set(li))  #중복제거

def quick_sort(li, first, last):
    if first >= last: return
    left, right = first + 1, last
    pivot = li[first]
    while left <= right:
        while left <= last and len(li[left]) <= len(pivot):
            if len(li[left]) != len(pivot):
                left += 1
            else:
                if li[left] > pivot: break
                else: left += 1
        while right > first and len(li[right]) >= len(pivot):
            if len(li[right]) != len(pivot):
                right -= 1
            else:
                if li[right] < pivot: break
                else: right -= 1
        if left <= right:
            li[left], li[right] = li[right], li[left]
            left += 1
            right -= 1
    li[first], li[right] = li[right], li[first]
    quick_sort(li, first, right - 1)
    quick_sort(li, right + 1, last)

quick_sort(li, 0, len(li) - 1)
for x in li:
    print(x)