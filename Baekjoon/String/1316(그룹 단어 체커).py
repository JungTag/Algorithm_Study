N = int(input())
cnt = 0

for _ in range(N):
    word = input()
    checker = set()
    last_char = ""
    for char in word:
        if char not in checker:
            checker.add(char)
            last_char = char
        else:
            if last_char != char:
                checker.add("BREAK")
                break
    if "BREAK" not in checker:
        cnt += 1
        
print(cnt)

    