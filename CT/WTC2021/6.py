def solution(time, plans):
    MONDAY_ATTANDANCE_TIME = 13
    FRIDAY_QUITTING_TIME = 18

    answer = ''
    
    for place, friday_departure_time, monday_arrival_time in plans:
        needed_time = 0
        friday_departure_time = convert_time_to_int(friday_departure_time, len(friday_departure_time))
        monday_arrival_time = convert_time_to_int(monday_arrival_time, len(monday_arrival_time))

        if friday_departure_time < FRIDAY_QUITTING_TIME:
            needed_time += FRIDAY_QUITTING_TIME - friday_departure_time
        if monday_arrival_time > MONDAY_ATTANDANCE_TIME:
            needed_time += monday_arrival_time - MONDAY_ATTANDANCE_TIME

        if needed_time <= time:
            answer = place
            break

    return answer


def convert_time_to_int(time, n):
    HALF_DAY = 12

    hours, unit = int(time[:n-2]), time[n-2:]

    if unit == 'AM':
        return hours
    else:
        return hours + HALF_DAY
    

print(solution(3.5, [["엘에이", "3PM", "2PM"], ["홍콩", "11PM", "9AM"]]))