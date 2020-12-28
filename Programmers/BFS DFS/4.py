def solution(tickets):
    answer, graph, START = [], {}, "ICN"
    for A, B in tickets:
        if A not in graph.keys():
            graph[A]= [[B,False]]
        else:
            graph[A].append([B,False])
            graph[A].sort(reverse = True)
    stack = [START] # graph[ICN] = [[vertex, isVisted]]
    while stack: 
        A = stack.pop() # 방문한 공항이름
        answer.append(A)
        for i in range(len(graph[A])):
            if graph[A][i][1] == False and graph[A][i][0] in graph.keys():
                graph[A][i][1] = True
                stack.append(graph[A][i][0])
        if not stack:
            for i in range(len(graph[A])):
                if graph[A][i][1] == False: 
                    answer.append(graph[A][i][0])
    return answer

# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
# print(solution(tickets))
tickets = [["ICN", "A"], ["A", "C"],["A", "D"], ["D", "B"], ["B", "A"]]
print(solution(tickets))
# tickets = [["ICN", "A"], ["ICN", "B"], ["B", "ICN"]]
# # print(solution(tickets))
# tickets = [["ICN", "A"], ["A", "ICN"], ["ICN", "A"]]
# print(solution(tickets))
# tickets = [['ICN','BOO' ], [ 'ICN', 'COO' ], [ 'COO', 'DOO' ], ['DOO', 'COO'], [ 'BOO', 'DOO'] ,['DOO', 'BOO'], ['BOO', 'ICN' ], ['COO', 'BOO']]
# print(solution(tickets))
tickets = [["ICN", "COO"], ["ICN", "BOO"],["COO", "ICN"], ["BOO", "DOO"]]
print(solution(tickets)) # ICN -> COO -> ICN -> BOO -> DOO