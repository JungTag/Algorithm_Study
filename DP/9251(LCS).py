import sys
str1 = list(sys.stdin.readline().strip())
str2 = list(sys.stdin.readline().strip())
LCS = [[0 for j in range(len(str2)+1)] for i in range(len(str1)+1)] 

for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
        if str1[i-1] == str2[j-1]:  # 문자열은 첫번째 글자(index:0)부터 검사해야 하므로
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

print(LCS[len(str1)][len(str2)])
