class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key) + '-' + str(self.value)

def search_key(root, key):
    if root == None:
        return None
    elif key == root.key:
        return root
    elif key < root.key:
        return search_key(root.left, key)
    else:
        return search_key(root.right, key)

def search_value(root, value):
    if root == None:
        return None
    elif root.value == value:
        return root
    
    res = search_value(root.left, value)
    if res is not None:
        return res
    else:
        return search_value(root.right, value)

def find_minKey(root):
    while root != None and root.left != None:
        root = root.left
    return root

def find_maxKey(root):
    while root != None and root.right != None:
        root = root.right
    return root

def insert(root, node):
    if node.key < root.key:
        if root.left == None:
            print(f'{node}는 {root}의 왼쪽 자식입니다.')
            root.left = node
            return True
        else:
            insert(root.left, node)

    elif node.key > root.key:
        if root.right == None:
            print(f'{node}는 {root}의 오른쪽 자식입니다.')
            root.right = node
            return True
        else:
            insert(root.right, node)
    else:
        return False # 중복 삽입 불가

def delete_case1(parent, root, node):
    if parent == None:
        root = None
    else:
        if node.key < parent.key:
            parent.left = None
        elif node.key > parent.key:
            parent.right = None
    return root

def delete_case2(parent, root, node):
    if node.left == None:
        child = node.right
    else:
        child = node.left

    if root == node:
        root = None
    elif parent.left == node:
        parent.left = child
    else:
        parent.right = child

    return root
    
def delete_case3(parent, root, node):
    toChangeNodesParent = node
    toChangeNode = node.right
    while toChangeNode.left != None:
        toChangeNodesParent = toChangeNode
        toChangeNode = toChangeNode.left
    
    if toChangeNodesParent.left == toChangeNode:
        toChangeNodesParent.left = toChangeNode.right
    else:
        toChangeNodesParent.right = toChangeNode.right
        
    node.key = toChangeNode.key
    node.value = toChangeNode.value
    
    return root

def findParentAndNodeWithKey(root, key):
    parent = None
    node = root
    while True:
        if node.key == key or node == None:
            break
        parent = node
        if node.key > key:
            node = node.left
        else:
            node = node.right
    return (parent, node)

def delete(root, key):
    parent, node = findParentAndNodeWithKey(root, key)
    if parent == None:
        return None
    elif node.left == None and node.right == None:
        return delete_case1(parent, root, node)
    elif node.left == None or node.right == None:
        return delete_case2(parent, root, node)
    else:
        return delete_case3(parent, root, node)

def displayWithLevel(root):
    if root == None:
        print(None)
    else:    
        level = 1
        nodeList = [root]
        childList = []

        while True:
            print(str(level)+':', end='')
            for node in nodeList:
                print(str(node) + ', ', end='')
            print('\n')

            for node in nodeList:
                if node.left != None:
                    childList.append(node.left)
                if node.right != None:
                    childList.append(node.right)
            
            if len(childList) == 0:
                print('end')
                break
            else:
                nodeList = childList
                childList = []
                level += 1