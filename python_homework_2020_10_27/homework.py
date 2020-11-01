# 이진탐색 맵에서 쓸 수정된 이진탐색 함수
def binary_search(A, key, low, high):
    if low <= high:
        middle = (low + high) // 2
        if key == A[middle].key:
            return A[middle]
        elif key > A[middle].key:
            return binary_search(A, key, middle + 1, high)
        else:
           return binary_search(A, key, low, middle-1)
    return None
    
# 엔트리 class
class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(f"{self.key}:{self.value}") # 연산자 오버로딩(Entry class 객체를 print하면 이렇게 나오도록 함.)

# 문제 1 : 이진탐색 맵
class binarySearchMap:
    def __init__(self):
        self.table = []

    def size(self):
        return len(self.table)

    def display(self, msg="Data Table="):
        if self.size() == 0:
            return None
        else:
            print(msg)
            for entry in self.table:
                print(" ", entry)

    def insert(self, key, value):
        entry = Entry(key, value)

        # 항목이 하나도 없거나 table에 저장된 Entry의 key값 중에 가장 크면 맨 뒤에 삽입. 
        # table에 저장된 entry들의 key값의 최대값을 알기 위해 key값만 모아놓은 리스트를 생성.
        if self.size() == 0 or key > max([x.key for x in self.table]):
            self.table.append(entry)

        else:
            for index in range(len(self.table)):
                beforeKey = self.table[index].key   # 새로 추가할 entry의 앞 entry
                afterKey = self.table[index + 1].key    # 새로 추가할 entry의 뒷 entry

                if beforeKey < key < afterKey:
                    # 새로 추가할 요소를 두 entry 사이에 끼워넣는 과정을 슬라이싱으로 구현.
                    self.table = self.table[:index + 1] + [entry] + self.table[index + 1:]
                    break

    def search(self, key):
        high = len(self.table) - 1
        # 이진탐색 함수 사용
        return binary_search(self.table, key, 0, high)

    def delete(self, key):
        # 클래스 안의 search() 재사용
        targetEntry = self.search(key)
        self.table.pop(self.table.index(targetEntry))

# 문제 2 : 선형조사법을 이용한 해시 맵
class HashLinearProbingMap:
    def __init__(self, mapSize):
        self.table = [None]*mapSize
        self.mapSize = mapSize

    # table의 index 장소가 사용가능한지 여부 판단(index 자리가  None이나 used라면~)
    def isAvailable(self, index):
        return self.table[index] == None or self.table[index] == "used"
    
    def isFull(self):
        return None not in self.table and "used" not in self.table

    def hashFn(self, key):
        sum = 0
        for c in key:
            sum = sum + ord(c)
        return sum % self.mapSize

    def insert(self, key, value):
        if self.isFull():
            print("Table is full!")
        else:
            entry = Entry(key, value)
            index = self.hashFn(key)
            if self.isAvailable(index):
                self.table[index] = entry
            else:
                while True:
                    # table을 순회하며 빈 자리를 찾음
                    index = (index + 1) % self.mapSize
                    if self.isAvailable(index):
                        self.table[index] = entry
                        break
                    
    def search(self, key):
        index = self.hashFn(key)
        count = 0
        # table이 포화상태일 때, 사용자가 존재하지 않는 key값을 입력하는 경우 무한 while문에 빠지는 문제 방지
        while count <= self.mapSize:
            # 종료 조건
            if self.table[index] == None:
                return None
            # 다음 index로...
            elif self.table[index] == "used":
                index = (index + 1) % self.mapSize
                count += 1
            # 종료 조건(탐색 성공)
            elif self.table[index].key == key:
                return self.table[index]
            # 다음 index로...
            elif self.table[index].key != key:
                index = (index + 1) % self.mapSize
                count += 1
        # 사용자가 존재하지 않는 key값을 입력했을 때 None 반환
        return None
            
    def delete(self, key):
        # class 내의 search()를 활용해서 해당 key의 entry 객체 받아오기
        entry = self.search(key)
        if entry == None:
            print(f"{key} is not in Table")
        else:
            deleteIndex = self.table.index(entry)
            # entry 삭제 후 index 자리에 사용 흔적 표시
            self.table[deleteIndex] = "used"

    def display(self, msg="Table:"):
        for entry in self.table:
            # 비어있는 부분 제외하고 출력
            if entry != None and entry != "used":
                print(entry)

# ---------------------------------------------------------
# binarySearchMap test
testClass = binarySearchMap()
# insert function test
testClass.insert(1, "apple")
testClass.insert(2, "banana")
testClass.insert(4, "mango")
# 리스트 중간 삽입 테스트
testClass.insert(3, "orange")
# display, size function test
testClass.display()
print(testClass.size())
# search function test
print(testClass.search(1))
#delete function test
testClass.delete(2)

# HashLinearProbingMap test
testHashMap = HashLinearProbingMap(5)
# insert function test
testHashMap.insert("사과", "apple")
testHashMap.insert("바나나", "banana")
testHashMap.insert("오렌지", "orange")
testHashMap.insert("망고", "mange")
testHashMap.insert("레몬", "lemon")
# isFull function test
testHashMap.insert("파인애플", "pineapple")
#display function test
testHashMap.display()
# search funtion test
print("검색 결과 -->", testHashMap.search("사과"))
# delete funtion test
testHashMap.delete("오렌지")
testHashMap.display()