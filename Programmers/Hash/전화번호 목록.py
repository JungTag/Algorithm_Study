def solution(phone_book):
    phone_book.sort(key=len)
    last = len(phone_book)
    for i in range(last):
        for j in range(i+1, last):
            cnt = 0
            for k in range(len(phone_book[i])):
                if phone_book[i][k] != phone_book[j][k]:
                    break
                else:
                    cnt += 1
            if cnt == len(phone_book[i]):
                answer = False
                return answer
    answer = True
    return answer