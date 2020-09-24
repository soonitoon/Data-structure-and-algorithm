# 2.1

def tax(pay):
    a = pay - 12*10**6 
    b = a - 34*10**6   
    c = b - 42*10**6  
    d = c - 62*10**6   

    tax_point = {"a":12*10**6, "b":46*10**6, "c":88*10**6, "d":15*10**7}
    tax_ratio = {"a":6/100, "b":15/100, "c":24/100, "d":35/100, "e":38/100}
    tax_dic = {i:tax_point[i]*tax_ratio[i] for i in "abcd"}

    if a <= 0:
        tax = int(pay*tax_ratio["a"])
        print("1구간")
        return f"세금: {tax}원, 세후 소득: {pay - tax}원"

    elif  b <= 0:
        tax = int(tax_dic["a"] + a*tax_ratio["b"])
        print("2구간")
        return f"세금: {tax}원, 세후 소득: {pay - tax}원"
    
    elif c <= 0:
        tax = int(tax_dic["a"] + tax_dic["b"] + b*tax_ratio["c"])
        print("3구간")
        return f"세금: {tax}원, 세후 소득: {pay - tax}원"
    
    elif d <= 0:
        tax = int(tax_dic["a"] + tax_dic["b"] + tax_dic["c"] + c*tax_ratio["d"])
        print("4구간")
        return f"세금: {tax}원, 세후 소득: {pay - tax}원"

    else:
        tax = int(tax_dic["a"] + tax_dic["b"] + tax_dic["c"] + tax_dic["d"] + d*tax_ratio["e"])
        print("5구간")
        return f"세금: {tax}원, 세후 소득: {pay - tax}원"

# 2.2

def guess_num():
    answer = 34
    min = 0
    max = 99
    count = 1

    for i in range(10):
        guess = int(input(f"숫자를 입력해주세요(범위: {min}~{max}): "))

        if guess == answer:
            break
        elif guess > answer:
            print("아닙니다, 더 작은 숫자입니다!")
            max = guess
        else:
            print("아닙니다, 더 큰 숫자입니다!")
            min = guess

        count += 1
    print(f"정답입니다. {count}번 만에 맞췄습니다." if count <= 10 else "횟수초과!")

# run

if __name__ == "__main__":
    print(tax(11*10**6))  # 1구간
    print(tax(21*10**6))  # 2구간
    print(tax(65*10**6))  # 3구간
    print(tax(90*10**6))  # 4구간
    print(tax(160*10**6)) # 5구간
    
    guess_num()


