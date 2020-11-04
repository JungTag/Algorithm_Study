def solution(routes):
    answer = 1
    routes.sort(key = lambda x: x[1])
    for i in range(1, len(routes)-1):
        start1, end1 = routes[i]
        start2, end2 = routes[i+1]
        if start1 <= start2 and start2 <= end1:
            answer += 1
        else:
            continue
    
    return answer

routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes))

print(solution([[-2,-1], [1,2],[-3,0]])) #2
print(solution([[0,0],])) #1
print(solution([[0,1], [0,1], [1,2]])) #1
print(solution([[0,1], [2,3], [4,5], [6,7]])) #4
print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])) #2
print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]])) #2
print(solution([[-20,15], [-20,-15], [-14,-5], [-18,-13], [-5,-3]])) #2