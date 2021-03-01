def gen_permutation(n, depth, P):
    result = []
    if depth == n:
        return [P]
    else:
        for i in range(len(arr)):
            if chosen[i] == True:
                continue
            chosen[i] = True
            result += gen_permutation(n, depth+1, P+[i])
            chosen[i] = False
    return result

# def gen_combinations(arr, n):
#     result =[] 

#     if n == 0: 
#         return [[]]

#     for i in range(0, len(arr)): 
#         elem = arr[i] 
#         rest_arr = arr[i + 1:] 
#         for C in gen_combinations(rest_arr, n-1): 
#             result.append([elem]+C) 
              
#     return result

# def gen_permutations(arr, n):
#     result = []

#     if n == 0:
#         return [[]]

#     for i, elem in enumerate(arr): 
#         for P in gen_permutations(arr[:i] + arr[i+1:], n-1):
#             result += [[elem]+P]
              
#     return result

arr = ['a', 'b', 'c', 'd', 'e']
arr = "012345"
chosen = [False for _ in range(len(arr))]
print(gen_permutation(4, 0, []))

def choose(n,k):
    if k == 0: 
       return 1
    elif n < k:
       return 0
    else:
        return choose(n-1, k-1) + choose(n-1, k)

print(choose(10,2))    