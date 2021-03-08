import sys
sys.setrecursionlimit(10**6)

def cal_queue(queue):
    result = queue[0]
    for i in range(0, len(queue)-2, 2):
        post = queue[i+2]
        result = cal_nums(result, post, queue[i+1])
    return result

def cal_nums(pre: int, post: int, op: str) -> int:
    if op == "+":
        return pre + post
    elif op == "-":
        return pre - post
    else:
        return pre * post

def insert_bracket(i, q):
    if i == n-1:
        no_br = q + [f[i]]
        return cal_queue(no_br)
    if i == n-3: # 한 번 더 갈 수 있음
        no_br = q + [f[i], f[i+1]]
        temp = cal_nums(f[i], f[i+2], f[i+1])
        br = q + [temp]
        return max(insert_bracket(i+2, no_br), cal_queue(br))

    # 안 넣는 경우
    no_br = q + [f[i], f[i+1]]

    # 넣는 경우
    temp = cal_nums(f[i], f[i+2], f[i+1])
    br = q + [temp, f[i+3]]

    return max(insert_bracket(i+2, no_br), insert_bracket(i+4, br))

n = int(sys.stdin.readline().strip())
f = [int(x) if x != "+" and x != "-" and x != "*" else x for x in sys.stdin.readline().strip()]

print(insert_bracket(0, []))

'''
def insert_bracket(i, q):
    # 안 넣는 경우
    if i < n-1:
        nq = q + [f[i], f[i+1]]
        no_br = insert_bracket(i+2, nq)
    else:
        nq = q + [f[i]]
        return cal_queue(nq)

    # 넣는 경우
    temp = cal_nums(f[i], f[i+2], f[i+1])
    if i+3 <= n-1:
        nq = q + [temp, f[i+3]]
        br = insert_bracket(i+4, nq)
    else: # 끝 부분
        nq = q + [temp]
        return cal_queue(nq)

    return max(no_br, br)
'''