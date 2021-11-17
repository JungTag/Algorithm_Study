def solution(leave, day, holidays):
    FIRST_OF_MONTH = 1
    LAST_OF_MONTH = 30
    answer = -1

    add_holidays(day, holidays)
    holidays_set = set(holidays)
    
    for start_day in range(FIRST_OF_MONTH, LAST_OF_MONTH+1):
        cnt = 0
        left_leave = leave
        for vacation_day in range(start_day, LAST_OF_MONTH+1):
            if vacation_day not in holidays_set:
                if left_leave > 0:
                    left_leave -= 1
                else:
                    break
            cnt += 1
        answer = max(answer, cnt)
        
    return answer

def add_holidays(day, holidays):
    LAST_OF_MONTH = 30
    weekend_start = {'MON': 6, 'TUE': 5, 'WED': 4, 'THU': 3, 'FRI': 2, 'SAT': 1, 'SUN': 7}
    weekend_start_day = weekend_start[day]

    if day == 'SUN':
        holidays.append(1)

    for day in range(weekend_start_day, LAST_OF_MONTH+1, 7):
        next_day = day+1
        if day <= LAST_OF_MONTH:
            holidays.append(day)
        if next_day <= LAST_OF_MONTH:
            holidays.append(next_day)

print(solution(4, "FRI", [6, 21, 23, 27, 28]))
print(solution(3, "SUN", [2, 6, 17, 29]))