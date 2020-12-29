'''
LPS = longest prefix suffix
패턴 미스매칭시 처음부터 다시 검색하는 게 아니라 LPS 테이블을 이용해서 몇 칸 뒤로 가서 다시 탐색 시도
'''
import sys
def compute_LPS(pattern, lps):
    leng = 0 # length of the previous longest prefix suffix

    # lps[0] is always 0
    i = 1
    while i < len(pattern):
        # 이전 인덱스에서 같았다면 다음 인덱스만 비교
        if pattern[i] == pattern[leng]:
            leng += 1
            lps[i] = leng
            i += 1
        else:
            if leng != 0:
                leng = lps[leng-1]
            else:
                lps[i] = 0
                i += 1

def KMP_Search(pattern, text):
    M = len(pattern)
    N = len(text)
    cnt = 0
    index_list = []

    lps = [0]*M

    i = 0 # index for text[]
    j = 0 # index for pattern[]

    compute_LPS(pattern, lps)
    while i < N:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        elif pattern[j] != text[i]:
            if j != 0:
                j = lps[j-1] # j-1까지는 일치했으므로 재검사
            else:
                i += 1
        # 패턴을 찾은 경우
        if j == M:
            cnt += 1
            index_list.append(i-(j-1))
            j = lps[j-1]

    print(cnt)
    print(*index_list)
    

T = sys.stdin.readline().rstrip()
P = sys.stdin.readline().rstrip()
KMP_Search(P, T)
