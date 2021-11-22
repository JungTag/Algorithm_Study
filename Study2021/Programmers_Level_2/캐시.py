# https://programmers.co.kr/learn/courses/30/lessons/17680

from collections import deque

# 원래 풀이
def solution(cacheSize, cities):
    CACHE_HIT = 1
    CACHE_MISS = 5

    answer = 0
    queue = deque([])

    if cacheSize == 0:
        return len(cities) * CACHE_MISS

    for city in cities:
        city = city.lower()

        if city in queue:
            queue.remove(city)
            queue.append(city)
            answer += CACHE_HIT
            
        if city not in queue:
            if len(queue) >= cacheSize:
                queue.popleft()
            queue.append(city)
            answer += CACHE_MISS

    return answer

# maxlen 이용
def solution(cacheSize, cities):
    CACHE_HIT = 1
    CACHE_MISS = 5

    answer = 0
    queue = deque([], maxlen=cacheSize)

    if cacheSize == 0:
        return len(cities) * CACHE_MISS

    for city in cities:
        city = city.lower()

        if city in queue:
            queue.remove(city)
            queue.append(city)
            answer += CACHE_HIT
            
        if city not in queue:
            queue.append(city)
            answer += CACHE_MISS

    return answer


print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
'''
cacheSize == 0일 때 고려를 안했다면 틀렸을듯
'''