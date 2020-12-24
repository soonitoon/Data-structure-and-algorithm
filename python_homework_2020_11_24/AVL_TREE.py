import BST

def rotateLL(root):
    leftNode = root.left
    root.left = leftNode.right
    leftNode.right = root
    return leftNode

def rotateRR(root):
    rightNode = root.right
    root.right = rightNode.left
    rightNode.left = root
    return rightNode

def rotateRL(root):
    rightNode = root.right
    root.right = rotateLL(rightNode)
    return rotateRR(root)

def rotateLR(root):
    leftNode = root.left
    root.left = rotateRR(leftNode)    
    return rotateLL(root)

def getHeight(root):
    if root == None:
        return 0
    level = 1
    nodeList = [root]
    childList = []
    while True:
        for node in nodeList:
            if node.left != None:
                childList.append(node.left)
            if node.right != None:
                childList.append(node.right)
        if childList == []:
            return level
        else:
            nodeList = childList
            childList = []
            level += 1

def getHeightDifference(root):
    if root == None:
        return 0
    left = getHeight(root.left)
    right = getHeight(root.right)
    return left - right

def reBalance(root):
    difference = getHeightDifference(root)
    if difference > 1:
        if getHeightDifference(root.left) > 0:
            root = rotateLL(root)
        else:
            root = rotateLR(root)
    elif difference < -1:
        if getHeightDifference(root.right) < 0:
            root = rotateRR(root)
        else:
            root = rotateRL(root)
    return root

def insert(parent, node):
    if node.key > parent.key:
        if parent.right == None:
            parent.right = node
        else:
            parent.right = insert(parent.right, node)
        return reBalance(parent)
        
    elif node.key < parent.key:
        if parent.left == None:
            parent.left = node
        else:
            parent.left = insert(parent.left, node)
        return reBalance(parent)

    else:
        print('키 중복 에러')

