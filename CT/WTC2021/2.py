import datetime 

def solution(log):
    MIN_STUDY_TIME = datetime.timedelta(minutes = 5)
    MAX_STUDY_TIME = datetime.timedelta(hours = 1 , minutes = 45)

    answer = datetime.timedelta(hours = 0, minutes = 0)
    start_time = ''
    end_time = ''

    for i, time in enumerate(log):
        if i % 2 == 0:
            start_time = time
        else:
            end_time = time
            time_diff = get_time_diff(start_time, end_time)

            if MIN_STUDY_TIME <= time_diff < MAX_STUDY_TIME:
                answer += time_diff
            elif time_diff >= MAX_STUDY_TIME:
                answer += MAX_STUDY_TIME

    # https://stackoverflow.com/questions/58937497/how-to-convert-a-python-timedelta-to-a-string-that-has-a-leading-zero-so-it-reta
    answer = "{:0>8}".format(str(answer))[:-3]

    return answer


def get_time_diff(start_time, end_time):
    start_time = datetime.datetime.strptime(start_time, "%H:%M")
    end_time = datetime.datetime.strptime(end_time, "%H:%M")

    return end_time - start_time


print(solution(["08:30", "09:00", "14:00", "16:00", "16:01", "16:06", "16:07", "16:11"]))