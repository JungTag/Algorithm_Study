import sys

def solve():
    result = 0

    for i, cur in enumerate(chars):
        if cur in open:
            stack.append(cur)
        elif cur in end:
            if stack:
                top = stack[-1]
            else:
                return 0
            if cur == ')':
                if top == '(':
                    stack.pop()
                    stack.append(2)
                else:
                    if not cal_inner('[', '(', 2):
                        return 0
            elif cur == ']':
                if top == '[':
                    stack.pop()
                    stack.append(3)
                else:
                    if not cal_inner('(', '[', 3):
                        return 0

    while stack:
        cur = stack.pop()
        if (cur in open) or (cur in end):
            return 0
        else:
            result += cur

    return result
    

def cal_inner(not_pair, pair, num):
    temp = 0

    while stack:
        top = stack[-1]
        if top == not_pair: # 짝이 맞지 않을 때
            return False
        elif top == pair: # 짝이 맞을 때
            stack.pop()
            temp *= num
            stack.append(temp)
            break
        else: # 숫자일 때
            temp += stack.pop()

    return temp


input = sys.stdin.readline
chars = input().strip()

stack = []
open = set(['(', '['])
end = set([')', ']'])

print(solve())
