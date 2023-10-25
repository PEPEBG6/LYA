from collections import deque

#Una clase para almacenar un nodo de arbol binario
class Node:
    def __init__(self, key=None, left=None, rigth=None):
        self.key=key
        self.left=left
        self.rigth=rigth
    
    def levelOrderTraversal(root):
        #Caja base
        if not root:
            return
        