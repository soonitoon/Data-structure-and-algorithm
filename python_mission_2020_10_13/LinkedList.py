class node:
  def __init__(self, element, link=None):
    self.element = element
    self.link = link

class LinkedList:
  def __init__(self):
    self.head = None
  
  def isEmpty(self):
    return self.head == None

  def clear(self):
    self.head = None

  def size(self):
    if not self.isEmpty():
      count = 0
      node = self.head
      while node != None:
        node = node.link
        count += 1
      
      return count

  def display(self, msg="LinkedList: "):
    if not self.isEmpty():
      node = self.head
      while node != None:
        print(node.element, "->", end="")
        node = node.link
      print("None")

  def getNode(self, pos):
    if pos < 0:
      return None
    else:
      while pos > 0 and node != None:
        node = node.link
        pos -= 1
      return node
    
  def getEntry(self, pos):
    node = self.getNode(pos)
    if node == None:
      return None
    else:
      return node.element

  def replace(self, pos, elem):
    node = self.getNode(pos)
    if node != None:
      node.data = elem

  def find(self, data):
    node = self.head
    while node != None:
      if node.element == data:
        return node
      else:
        node = node.link

  def insert(self, pos, elem):
    before = self.getNode(pos - 1)
    if before == None:
      self.head = node(elem, self.head)
    else:
      node = node(elem, before.link)
      before.link = node

  def delete(self, pos):
    before = self.getNode(pos - 1)
    if before == None:
      if self.head != None:
        self.head = self.head.link
    elif before.link != None:
      before.link = before.link.link
