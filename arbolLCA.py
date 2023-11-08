class TreeNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

def findLCA(root, name1, name2):
    if root is None:
        return None
    
    if root.name == name1 or root.name == name2:
        return root
    
    left_lca = findLCA(root.left, name1, name2)
    right_lca = findLCA(root.right, name1, name2)
    
    if left_lca and right_lca:
        return root
    if left_lca:
        return left_lca
    else:
        return right_lca







# Crear un árbol binario de ejemplo con nombres
root = TreeNode("Uziel 1")
root.left = TreeNode("Jesus")
root.left.left = TreeNode("José")
root.left.right = TreeNode("Luis Miguel")
root.left.left.left=TreeNode("Christian")
root.left.left.right=TreeNode("Xavier")
root.left.right.left=TreeNode("Lionel")
root.left.right.right=TreeNode("Cristiano R")
root.left.left.left.left=TreeNode("Michael")
root.left.left.right.left=TreeNode("Barak")
root.left.right.left.left=TreeNode("Ronaldinho")
root.left.right.left.right=TreeNode("Dana")
root.left.right.right.left=TreeNode("Cristian N")
root.left.right.right.right=TreeNode("Diego")
root.left.left.right.left.left=TreeNode("George")
root.left.left.right.left.right=TreeNode("Kalea")
root.left.right.left.right.left=TreeNode("Goku")
root.left.right.right.left.left=TreeNode("Benito")
root.left.right.left.right.left.left=TreeNode("Gohan")
root.left.right.left.right.left.right=TreeNode("Goten")
root.left.right.right.left.left.left=TreeNode("Daniel")
root.left.right.right.left.left.right=TreeNode("Kevin")
root.left.right.left.right.left.left.left=TreeNode("Pan")
root.left.right.left.right.left.left.left.left=TreeNode("Pan")

root.right = TreeNode("Graciela")
root.right.left = TreeNode("Valentina")
root.right.right = TreeNode("Alfredo")
root.right.left.left=TreeNode("Magi")
root.right.left.right=TreeNode("Bart")
root.right.right.left=TreeNode("Joaquin")
root.right.right.right=TreeNode("Juan")
root.right.left.left.left=TreeNode("Brayan")
root.right.left.left.right=TreeNode("ValentinaII")
root.right.right.left.left=TreeNode("Arturo")
root.right.right.right.left=TreeNode("Melchor")
root.right.left.left.left.left=TreeNode("kimberli")
root.right.left.left.left.right=TreeNode("Britani")
root.right.left.left.right.left=TreeNode("Alex")
root.right.left.left.right.right=TreeNode("Penelope")
 



# Encontrar el LCA de dos nodos con nombres
name1 = "Hijo1"
name2 = "Hijo2"
lca = findLCA(root, name1, name2)
print(f"El LCA de {name1} y {name2} es: {lca.name}")
