def solution(jobs):
    number_of_jobs = len(jobs)
    result = []; disk =[]; curr_time = 0
    jobs.sort(key = lambda x: (x[0], x[1]))
    # jobs[i][0], jobs[i][1] = request_time, lead_time
    while jobs or disk:
        if disk:
            print(f"jobs: {jobs}")
            print(f"disk: {disk}")
            print(f"result: {result}")
            task_on_disk = disk.pop()
            curr_time += task_on_disk[1]; elapsed_time = curr_time - task_on_disk[0]
            result.append(elapsed_time)
            if jobs:
                min_pair = [float('inf'), 0] # (value, index)
                for i in range(len(jobs)):
                    if jobs[i][0] <= curr_time:  # request_time <= curr_time
                        if curr_time - jobs[i][1] < min_pair[0]:
                            min_pair[0], min_pair[1] = curr_time - jobs[i][1], i
                disk.append(jobs[min_pair[1]]); 
                del jobs[min_pair[1]]
        else: # 디스크가 작업을 수행하고 있지 않을 때, 즉 맨 처음
            disk.append(jobs.pop(0))
    answer = sum(result) // number_of_jobs
    print(result)
    return answer
'''
            print(f"jobs: {jobs}")
            print(f"disk: {disk}")
            print(f"result: {result}")
'''

'''
def solution(jobs):
    jobs.sort(key = lambda x: (x[0], x[1]))
    number_of_jobs = len(jobs); time = 0
    while jobs:
        request_time, lead_time = 
    return answer
'''

'''
import heapq as hq

def solution(jobs):
    n = len(jobs)
    result = []; disk =[]; curr_time = 0
    for i in range(len(jobs)):
        request_time, lead_time = jobs[i]
        jobs[i][0], jobs[i][1] = lead_time, request_time
    while jobs or disk:
        if disk:
            curr_time += 1
            task_on_disk = disk[0] # disk[x] = [소요시간, 요청시간, 입장시간]
            lead_time, request_time, entry_time = task_on_disk[0], task_on_disk[1], task_on_disk[2]
            if curr_time - entry_time == lead_time:
                result.append(curr_time - request_time)
                disk.pop()
                if jobs:
                    if jobs[0][1] <= curr_time:
                        disk.append(hq.heappop(jobs))
                        disk[0].append(curr_time) # 입장시간 추가
                else:
                    break
        else: # 디스크가 작업을 수행하고 있지 않을 때, 즉 맨 처음
            jobs[0].append(curr_time)
            disk.append(jobs.pop(0))
            hq.heapify(jobs)
    answer = sum(result) // n
    return answer
'''