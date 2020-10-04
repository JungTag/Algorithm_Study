from collections import deque
import heapq as hq

def solution(operations):
    queue = []
    operations = deque(operations)
    while operations:
        op = operations.popleft()
        command, num = op.split(); num = int(num)
        if command == "I":
            hq.heappush(queue, num)
        if command == "D" and queue:
            if num == -1:
                hq.heappop(queue)
            else:
                max_num = max(queue[len(queue)//2:])
                queue.remove(max_num)
    if queue:
        max_num = max(queue[len(queue)//2:])
        answer = [max_num, queue[0]]
    else:
        answer = [0, 0]
    return answer