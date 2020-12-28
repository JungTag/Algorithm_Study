import sys

n = int(input())
input_list = [sys.stdin.readline().rstrip() for i in range(n)]
li =[]


for x in input_list:
    li.append(list(map(int, x.split()))) #좌표를 리스트로 만들어 li에 append
def quick_sort(li, first, last):
    if first >= last: return
    pivot = li[first]
    left, right = first + 1, last
    while left <= right:
        while left <= last and li[left] < pivot:
            left += 1
        while right > first and li[right] > pivot:
            right -= 1
        if left <= right:
            li[left], li[right] = li[right], li[left]
            left += 1
            right -= 1
    li[first], li[right] = li[right], li[first]
    quick_sort(li, first, right-1)
    quick_sort(li, left, last)

quick_sort(li, 0, len(li)-1)
for x, y in li:
    print(x, y)

'''
풀이: in-place한 방식의 quick sort이용
1) 리스트를 만들어 병합하는 방식의 not in-place한 방식의 quick sort는 
너무 많은 재귀호출과 메모리 필요, 따라서 in-place한 방식의 quick sort사용
2) x와 y를 나눠서 정렬해야 된다는 생각 때문에 시간을 버림
리스트 자료형은 원소 순서짝대로 서로 비교(line 15, 17)하기 때문에 알아서 정렬됨

의문:
for x, y in li:
    print(x, y) <-- 이건 되는데
    
for x in li: print
    print(x[0], x[1]) <-- 이건 왜 안 될까?

깨달은 점:
- 많은 입력을 요할 땐 sys.stdin을 사용하자
- not-in place한 알고리즘 사용을 자제하자
''' 


        
