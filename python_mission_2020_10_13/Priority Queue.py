class PriorityQueue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def findMaxIndex(self):
        if self.isEmpty():
            return None
        else:
            highest = 0
            for i in range(self.size()):
                if self.items[i] > self.items[highest]:
                    highest = i
            
            return highest
    
    def dequeue(self):
        highest = self.findMaxIndex()
        if highest != None:
            return self.items.pop(highest)
    
    def peek(self):
        highest = self.findMaxIndex()
        if highest != None:
            return self.items[highest]

# run
pq = PriorityQueue()
for i in range(10):
    pq.enqueue(i)
print(pq.size())
print(pq.items)
print(pq.dequeue())
print(pq.items)
