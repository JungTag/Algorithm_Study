import sys
n = int(sys.stdin.readline().strip())
num_list = [int(x) for x in sys.stdin.readline().split()]
op_list = [int(x) for x in sys.stdin.readline().split()]
solution_set = set()

def calculate(total, num, op):
    # op_list = [+, -, x, //]
    if op == 0:
        return total + num
    elif op == 1:
        return total - num
    elif op == 2:
        return total * num
    else:
        if total < 0:
           return -(-(total) // num)
        return total // num

def make_expression(depth, pre_total, op_list):
    if depth == n:
        solution_set.add(pre_total)
        return
    num = num_list[depth]
    for i in range(4):
        if op_list[i] > 0:
            current_total = calculate(pre_total, num, i)
            copy_list = op_list[:]
            copy_list[i] -= 1
            make_expression(depth+1, current_total, copy_list)

make_expression(1, num_list[0], op_list)
print(max(solution_set))
print(min(solution_set))