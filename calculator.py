sum = 0
total = 0

while True:
    try:
        credit = int(input('학점을 입력하세요. '))
        score = float(input('환산 점수를 입력하세요. '))
        sum += score*credit
        total += credit
    except:
        break

print(f"누적 점수는 {sum}입니다.")
print(f"평균학점은 {sum/total}입니다.")
