from circularQ_practice import CircularQueue, MAX_QSIZE 

class circular_deque(CircularQueue):
  def __init__(self):
    super().__init__()
  
  # overwriting
  def addRear(self, item):
    self.enqueue(item)
  
  def deleteFront(self):
    return self.dequeue()
  
  def getFront(self):
    return self.peek()
  
  # new function
  def addFront(self, item):
    if not self.isFull():
      self.items[self.front] = item

      if self.front == 0:
        self.front = MAX_QSIZE - 1
      else:
        self.front = self.front - 1
      
  def deleteRear(self):
    if not self.isEmpty():
      item = self.items[self.rear]

      if self.rear == 0:
        self.rear = MAX_QSIZE - 1
      else:
        self.rear = self.rear - 1
      return item

  def getRear(self):
    if not self.isEmpty():
      return self.items[self.rear]