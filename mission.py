# 미션 1
# 1-1
for i in range(1, 10):
    print(f"7 * {i} = {7*i}")

# 1-2
i = 1
while i <= 9:
    print(f"7 * {i} = {7*i}")
    i += 1

# 1-3
# for문
for i in range(9, 0, -1):
    print(f"6 * {i} = {6*i}")
# while문
i = 9
while i >= 1:
    print(f"6 * {i} = {6*i}")
    i -= 1

# 미션 2
def f_to_c(f):
    return (f -32)*100/180
print(f_to_c(72))

# 미션 3-1
LIST_A = [1, 2, 3, 4]
LIST_A.reverse()
print(LIST_A)
# 미션 3-2
LIST_A = [1, 2, 3, 4]
def sum_list(list_a):
    return sum(list_a)
print(sum_list(LIST_A))

# 미션 4-1
msg = "Data Structures in Python"
print(msg)
print(msg.upper())
print(msg.lower())

# 미션 5-1
price = { "콩나물 해장국" : 4500, "갈비탕" : 9000, "돈까스" : 8000 }
price["팟타이"]=7000
print(price)
# # 미션 5-2
price = {i:x-500 for (i, x) in price.items()}
print(price)
print(sum([price[i] for i in price]))

# 미션 6-1
def sum_num(n):
    if n <= 1:
        return 1
    return n  + sum_num(n-1)
print(sum_num(10))
# 미션 6-2
def reverse_str(string):
    return string[::-1]
print(reverse_str("안녕하세요"))