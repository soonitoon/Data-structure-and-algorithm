import BST_MAP
import AVL_TREE
import BST

class AVLMap(BST_MAP.BSTMap):
    def __init__(self):
        super().__init__()

    def insert(self, key, value=None):
        node = BST.BSTNode(key, value)
        if self.isEmpty():
            self.root = node
        else:
            self.root = AVL_TREE.insert(self.root, node)
        
    def display(self, msg='AVLMap :'):
        BST.displayWithLevel(self.root)