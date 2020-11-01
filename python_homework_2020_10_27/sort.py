# 선택정렬 알고리즘 실습
def selectionSort(notSortedList):
    listLength = len(notSortedList)
    for i in range(listLength - 1):
        minimum = i
        for j in range(i+1, listLength):
            if notSortedList[j] < notSortedList[minimum]:
                minimum = j
        notSortedList[i], notSortedList[minimum] = notSortedList[minimum], notSortedList[i]
        printStep(notSortedList, i+1)

# 삽입정렬 연습
def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j=j - 1
            A[j+1] = key
        printStep(A, i)

# 버블정렬 연습
def bubbleSort(A):
    n = len(A)
    for i in range(n-1, 0, -1):
        bChanged = False
        for j in range(i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                bChanged = True
        if not bChanged:
            break
        printStep(A, n-i)

# 순차탐색 알고리즘
def SequentialSearch(A, key, low, high):
    for i in range(low, high+1):
        if key == i:
            return i
    return None

# 이진탐색 알고리즘
def binary_search(A, key, low, high):
    if low <= high:
        middle = (low + high) // 2
        if key == A[middle]:
            return middle
        elif key > A[middle]:
            return binary_search(A, key, middle + 1, high)
        else:
           return binary_search(A, key, low, middle-1)
    return None
        
# 보간탐색 알고리즘
def interpolation_search(A, key, low, high):
    if low <= high:
        middle = int(low + (high-low)*(key-A[low])/(A[high]-A[low]))
        if key == A[middle]:
            return middle
        elif key > A[middle]:
            return binary_search(A, key, middle + 1, high)
        else:
           return binary_search(A, key, low, middle-1)
    return None

def printStep(arr, val):
    print(f"Step {val} = ", arr)

# run
testList = [1,4,52,9,43,7,2,3,6]
selectionSort(testList)
print("end")
testList = [1,4,52,9,43,7,2,3,6]
insertionSort(testList)
print("end")
testList = [1,4,52,9,43,7,2,3,6]
bubbleSort(testList)
print("end")
result=binary_search(testList, 52, 0, len(testList) - 1)
print(result)
result = interpolation_search(testList, 52, 0, len(testList) - 1)
print(result)