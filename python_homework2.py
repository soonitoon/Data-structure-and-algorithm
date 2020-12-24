# 실습 1 : 배열 구조로 리스트 함수 구현
items =[]
def insert(pos, e):
    items.insert(pos, e)
def delete(pos):
    return items.pop(pos)
def get_entry(pos):
    return items[pos]
def is_empty():
    return len(items) == 0
def size():
    return len(items)
def clear():
    global items
    items = []
def find(item):
    return items.index(item)
def replace(pos, item):
    items[pos] = item
def sort():
    items.sort()
def merge(lst):
    items.extend(lst)
def display(msg='list:'):
    print(msg, size(), items)

print("실습 1 : 배열 구조로 리스트 함수 구현\n")
display('초기 리스트')
insert(1, 3)
delete(0)
insert(1, 3)
get_entry(0)
is_empty()
size()
clear()
insert(0, 1)
find(1)
replace(0, 2)
insert(1, 5)
sort()
merge([1,4,5])
display('실행 결과')

# 실습 1-2 : 클래스로 구현한 리스트
class lst:
    def __init__(self):
        self.items =[]
    def insert(self, pos, e):
        self.items.insert(pos, e)
    def delete(self, pos):
        return self.items.pop(pos)
    def get_entry(self, pos):
        return self.items[pos]
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def clear(self):
        self.items = []
    def find(self, item):
        return self.items.index(item)
    def replace(self, pos, item):
        self.items[pos] = item
    def sort(self):
        self.items.sort()
    def merge(self, lst):
        self.items.extend(lst)
    def display(self, msg='list:'):
        print(msg, self.size(), self.items)

print("\n실습 1-2 : 클래스로 구현한 리스트\n")
lst = lst()
lst.display('클래스로 구현한 초기 리스트')
lst.insert(1, 3)
lst.delete(0)
lst.insert(1, 3)
lst.get_entry(0)
lst.is_empty()
lst.size()
lst.clear()
lst.insert(0, 1)
lst.find(1)
lst.replace(0, 2)
lst.insert(1, 5)
lst.sort()
lst.merge([1,4,5])
lst.display('클래스로 구현한 실행 결과')

# 실습 2 라인 편집기
def line_edit():
    txt = []
    while True:
        menu = input("[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일 읽기, s-저장, q-종료")
        if menu == "i":
            pos = int(input("입력행 번호: "))
            line = input("입력행 내용: ")
            txt.insert(pos, line)
        elif menu == "d":
            pos = int(input("삭제행 번호: "))
            txt.pop(pos)
        elif menu == "r":
            pos = int(input("변경행 번호: "))
            line = input("변경행 내용: ")
            txt[pos] = line
        elif menu == "p":
            for i, text in enumerate(txt):
                print(i, text)
        elif menu == "l":
            file_name = input("열 파일 이름: ")
            with open(file_name, "r", encoding="utf-8") as f:
                txt = [text.strip("\n") for text in f.readlines()]
        elif menu == "s":
            with open("save.txt", "w", encoding="utf-8") as f:
                for line in txt:
                    f.write(line+"\n")
        elif menu == "q":
            break

print("\n실습 2 라인 편집기\n")
line_edit()

# 교재실습 3 : 집합의 구현
class Set:
    def __init__(self):
        self.items = []
  
    def size(self):
        return len(self.items)

    def contains(self, e):
        return e in self.items
  
    def insert(self, e):
        if e not in self.items:
            self.items.append(e)

    def delete(self, e):
        return self.items.pop(self.items.index(e))

    def equals(self, setB):
        return set(self.items) == set(setB)
  
    def union(self, setB):
        return set(self.items + setB)

    def intersect(self, setB):
        return [x for x in self.items if x in setB]

    def difference(self, setB):
        return [x for x in self.items if x not in setB]

    def display(self):
        print(self.items)

print("\n교재실습 3 : 집합의 구현\n")
setA = Set()
setA.insert(1)
setA.insert(1)
setA.insert(2)
setA.insert(3)
setA.insert(4)
setA.insert(5)
setA.display()
print(setA.delete(1))
setA.display()
print(setA.size())
print(setA.contains(2))
setB = [2,3,4,5]
print(setA.equals(setB))
setB = [2,3,4,6]
print(setA.equals(setB))
setB = [3,4,5,6]
print(setA.union(setB))
print(setA.intersect(setB))
print(setA.difference(setB))

# 미션 1 : 리스트 내의 최대값 찾기 함수
def find_max(lst):
    max = lst[0]
    
    for element in lst:
        if element > max:
            max = element
    
    return max

test_list = [4,5,6,2,3]

print("\n미션 1 : 리스트 내의 최대값 찾기 함수\n")
print(find_max(test_list))

# 미션 2 : 리스트 내 최소값 최대값 동시 반환 함수
def find_min_max(lst):
    max = lst[0]
    min = lst[0]

    for element in lst:
        if element > max:
            max = element
        if element < min:
            min = element
    
    return min, max

test_list = [4,5,6,2,3]

print("\n미션 2 : 리스트 내 최소값 최대값 동시 반환 함수\n")
print(find_min_max(test_list))

# 미션 3 : 리스트 동일 항목 여부 리턴 함수
def find_same_element(listA, listB):
    if len(set(listA) & set(listB)) > 0:
        return True
    else:
        return False

test_listA = [4,5,6,2,3]
test_listB = [7,6,8,7,8]

print("\n미션 3 : 리스트 동일 항목 여부 리턴 함수\n")
print(find_same_element(test_listA, test_listB))

# 미션 4 : 리스트 병합 함수 구현
def sort_list(listA, listB):
    return sorted(listA + listB)

test_listA = [1,2,3,4]
test_listB = [5,6,7,8]

print("\n미션 4 : 리스트 병합 함수 구현\n")
print(sort_list(test_listA, test_listB))

# 미션 5 : 진부분 집합인지 검사하는 메소드 추가
class Set:
    def __init__(self):
        self.items = []
  
    def size(self):
        return len(self.items)

    def contains(self, e):
        return e in self.items
  
    def insert(self, e):
        if e not in self.items:
            self.items.append(e)

    def delete(self, e):
        return self.items.pop(self.items.index(e))

    def equals(self, setB):
        return set(self.items) == set(setB)
  
    def union(self, setB):
        return set(self.items + setB)

    def intersect(self, setB):
        return [x for x in self.items if x in setB]

    def difference(self, setB):
        return [x for x in self.items if x not in setB]

    def display(self):
        print(self.items)

    def check_proper(self, listB):
        return set(self.items) & set(listB) == set(self.items) and self.items != listB

print("\n미션 5 : 진부분 집합인지 검사하는 메소드 추가\n")
setA = Set()
setA.insert(1)
setA.insert(2)
setB = [1,2,3]
print(setA.check_proper(setB))