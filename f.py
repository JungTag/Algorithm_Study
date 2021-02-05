import sys, collections

def cal_queue(q: collections.deque) -> int:
    result = q.popleft()
    temp = ""

    while q:
        cur = q.popleft()
        if cur != int:
            temp = cur
        else:
            result = cal_nums(result, cur, temp)

    return result

def cal_nums(pre: int, post: int, op: str) -> int:
    if op == "+":
        return pre + post
    elif op == "-":
        return pre - post
    else:
        return pre * post

def insert_bracket(idx: int, cnt: int, q: collections.deque):
    if cnt > limit or idx >= n-1:
        return cal_queue(q)

    # 묶는다면
    # temp = cal_nums(f[idx], f[idx+2], f[idx+1]) # 연산
    # if idx + 3 <= n-1:
    #     nq = q + collections.deque([temp]) + collections.deque([f[idx+3]])
    # else:
    #     nq = q + collections.deque([temp])
    # br = insert_bracket(idx+4, cnt+1, nq)

    # 안묶는다면
    if idx + 3 <= n-1:
        nq = q + collections.deque([f[idx]]) + collections.deque([f[idx+1]]) + collections.deque([f[idx+2]])
    else:
        nq = q + collections.deque([f[idx]]) + collections.deque([f[idx+1]]) + collections.deque([f[idx+2]])
        no_br = insert_bracket(idx+3, cnt, nq)

    return max(br, no_br)
    
n = int(sys.stdin.readline().strip())
f = [int(x) if x != "+" and x != "-" and x != "*" else x for x in sys.stdin.readline().strip()]

limit = n//2

print(insert_bracket(0, 0, collections.deque([])))
