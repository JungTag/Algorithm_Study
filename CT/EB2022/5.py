import sys
sys.setrecursionlimit(10**6)


def solution(P):
    ans = []
    MAX_LEN = len(P)

    dfs(P, MAX_LEN, set(), set(), ans, '', 0, MAX_LEN//2, MAX_LEN)

    return ans


def dfs(P, MAX_LEN, removed, visited, ans, matched_by_first, cur_depth, max_depth, rest_cnt):
    if cur_depth == max_depth:
        if rest_cnt == 0:
            ans.append(matched_by_first)

    for i in range(MAX_LEN):
        if i in removed:
            continue

        for j in range(i+1, MAX_LEN):
            if j in removed or (i, j) in visited:
                continue

            removed.add(i)
            removed.add(j)
            visited.add((i, j))

            if i == 0:
                matched_by_first = P[j]

            if is_palindrome(P[i]+P[j]) or is_palindrome(P[j]+P[i]):
                dfs(P, MAX_LEN, removed, visited, ans, matched_by_first, cur_depth+1, max_depth, rest_cnt-2)

            removed.remove(i)
            removed.remove(j)


def is_palindrome(string):
    if string == string[::-1]:
        return True
    return False


print(solution(["11","111","11","211"]))