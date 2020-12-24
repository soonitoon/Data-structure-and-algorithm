import BST

class BSTMap:
    def __init__(self):
        self.root = None

    def isEmpty(self): 
        return self.root == None

    def clear(self):
        self.root = None

    def size(self):
        if self.isEmpty:
            return 0
        else:
            count = 0
            nodeList = [self.root]
            childList = []
            while True:
                currentCount = len(nodeList)
                count += currentCount
                for node in nodeList:
                    if node.left != None:
                        childList.append(node.left)
                    if node.right != None:
                        childList.append(node.right)

                if childList == []:
                    break
                else:
                    nodeList = childList
                    childList = []

            return count 

    def search(self, key):
        return BST.search_key(self.root, key)

    def searchValue(self, value):
        return BST.search_value(self.root, value)

    def findMax(self):
        return BST.find_maxKey(self.root)

    def findMin(self):
        return BST.find_minKey(self.root)

    def insert(self, key, value=None):
        newNode = BST.BSTNode(key, value)
        if self.isEmpty():
            self.root = newNode
        else:
            BST.insert(self.root, newNode)

    def delete(self, key):
        return BST.delete(self.root, key)

    def display(self):
        BST.displayWithLevel(self.root)
