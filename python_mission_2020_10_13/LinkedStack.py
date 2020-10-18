class node:
  def __init__(self, element, link=None):
    self.element = element
    self.link = link

class LinkedStack:
  def __init__(self):
    self.top = None

  def isEmpty(self):
    return self.top == None
      
  def clear(self):
    self.top = None

  def push(self, item):
    n = node(item, self.top)
    self.top = n

  def pop(self):
    n = self.top
    self.top = n.link
    return n.element

  def size(self):
    if not self.isEmpty():
      count = 0
      node = self.top

      while node != None:
        node = node.link
        count += 1
      
      return count

  def display(self, msg="LinkedStack: "):
    if not self.isEmpty():
      node = self.top

      while node != None:
        print(node.element, "->", end="")
        node = node.link
      print("None")