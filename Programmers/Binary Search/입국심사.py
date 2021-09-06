def solution(n, times):
    answer = 0
    left, right = 0, n * times[-1]

    while left <= right:
        mid = (left + right) // 2  # mid = 기준시간
        cnt = 0   # cnt = 기준시간 내에 각 심사관이 심사할 수 있는 사람 수의 합
        for time in times:
            cnt +=  mid // time 
            if cnt >= n:
                break
        if cnt < n:
            left = mid + 1
            mid = right - 1
        else:
            answer = mid
            right = mid - 1

    return answer