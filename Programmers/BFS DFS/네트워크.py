def solution(n, computers):
    answer = 0; visited = [False] * n
    stack = [computers[0]]; visited[0] = True
    while stack:
        elem = stack.pop()
        for i in range(len(elem)):
            if elem[i] == 1 and visited[i] == False:
                visited[i]= True
                stack.append(computers[i])
        answer += [0, 1][not stack]
        if not stack and False in visited:
            i = visited.index(False); stack.append(computers[i])
    return answer

# def solution(n, computers):
#     answer = 0; visited = [False] * n
#     stack = [computers[0]]; visited[0] = True
#     while stack:
#         elem = stack.pop()
#         for i in range(len(elem)):
#             if elem[i] == 1 and visited[i] == False:
#                 visited[i]= True
#                 stack.append(computers[i])
#         answer += [0, 1][not stack]
#         if not stack :
#             for i in range(n):
#                 if not visited[i]: 
#                     stack.append(computers[i])
#                     break  # break를 안하면 방문안한 노드들을 다 추가해주므로 안된다!
#     return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])) # 2
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])) # 1 
print(solution(3, [[1, 0, 0], [0, 1, 0], [0, 0, 1]])) # 1 