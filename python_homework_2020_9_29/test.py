[최현오] [오후 3:47] import random
number = random.randint(1,999)
print(number)
 
while True: 
    try:                                 #정상적인 코드
        guess = int(input('숫자를 입력하세요 :'))
        if guess == number:
            print('정답입니다')
            break
        elif guess > number:
            print('더 작은 수 입니다')
        else:
            print('더 큰 수 입니다.')
    except:                              # 오류가 났을때 실행할 코드
        print('1-999중의 숫자를 입력하세요')