from collections import deque

def solution(n, record):
    server_dict = { i: deque([], 5) for i in range(1, n+1)}
    answer = []

    for r in record:
        server_num, char_name = r.split()
        server_num = int(server_num)

        if char_name not in server_dict[server_num]:
            server_dict[server_num].append(char_name)
    
    for queue in server_dict.values():
        for char_name in queue:
            answer.append(char_name)

    return answer

# print(solution(1, ["1 fracta", "1 sina","1 hana","1 robel","1 abc", "1 sina", "1 lynn"]))
# print(solution(4, ["1 a","1 b","1 abc","3 b","3 a","1 abcd","1 abc","1 aaa","1 a","1 z","1 q", "3 k", "3 q", "3 z", "3 m", "3 b"]))
print(solution(1, ["1 fracta"]))