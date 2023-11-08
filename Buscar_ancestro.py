class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Crear el árbol con nodos predefinidos
root = TreeNode("Xavier")
root.left = TreeNode("Marte")
root.right = TreeNode("Venus")
root.left.left = TreeNode("Romulo")
root.left.right = TreeNode("Remo")
root.right.left = TreeNode("Cupid")
root.right.right = TreeNode("Aeneas")
root.left.left.left = TreeNode("Numa")
root.left.left.right = TreeNode("Tito")
root.left.right.left = TreeNode("Faustulus")
root.left.right.right = TreeNode("Hersilia")
root.right.left.left = TreeNode("Psyche")
root.right.left.right = TreeNode("Ascanius")
root.right.right.left = TreeNode("Lavinia")
root.right.right.right = TreeNode("Pompilia")
root.left.left.left.left = TreeNode("Hostus")
root.left.left.left.right = TreeNode("Tullia")
root.left.left.right.left = TreeNode("Acca")
root.left.left.right.right = TreeNode("Voluptas")
root.left.right.left.left = TreeNode("Hedone")
root.left.right.left.right = TreeNode("Iulus")
root.left.right.right.left = TreeNode("Silvius")
root.left.right.right.right = TreeNode("Marica")
root.right.left.left.left = TreeNode("Numitor")
root.right.left.left.right = TreeNode("Rhea")
root.right.left.right.left = TreeNode("Amulius")
root.right.left.right.right = TreeNode("Ilia")
root.right.right.left.left = TreeNode("Rea Silvia")
root.right.right.right.left = TreeNode("Rómulo")
root.left.left.left.left.left = TreeNode("Brutus")
root.left.left.left.left.right = TreeNode("Alba")
root.left.left.right.left.left = TreeNode("Roma")
root.left.left.left.left.left.left = TreeNode("Augustus")
root.left.left.left.left.left.right = TreeNode("Julius")
root.left.left.left.left.right.left = TreeNode("Quintus")
root.left.left.left.left.right.right = TreeNode("Lucius")
root.left.left.right.left.right = TreeNode("Octavius")
root.left.left.right.left.right.left = TreeNode("Calpurnia")
root.left.left.right.left.right.right = TreeNode("Maximus")
root.left.left.right.left.right.left.left = TreeNode("Valeria")
root.left.left.right.left.right.left.right = TreeNode("Marcellus")
root.left.left.right.left.right.right.left = TreeNode("Julia")
root.left.left.right.left.right.right.right = TreeNode("Marcus")
root.left.left.left.left.right.left = TreeNode("Publius")
root.left.left.left.left.right.left.left = TreeNode("Livia")
root.left.left.left.left.right.left.left.left = TreeNode("Germanicus")
root.left.left.left.left.right.left.right = TreeNode("Claudius")
root.left.left.left.left.right.right = TreeNode("Caligula")
root.left.left.left.left.right.right.left = TreeNode("Nero")
root.left.left.left.left.right.right.left.left = TreeNode("Agrippina")
root.left.left.left.left.right.right.left.left.left = TreeNode("Britannicus")
root.left.left.left.left.right.right.left.right = TreeNode("Messalina")
root.left.left.left.left.right.right.left.right.left = TreeNode("Titus")
root.left.left.left.left.right.right.left.right.right = TreeNode("Domitia")

def find_common_ancestor(root, values):
    if root is None:
        return None

    if root.value in values:
        return root  # Devuelve el nodo en lugar de su valor

    left_ancestor = find_common_ancestor(root.left, values)
    right_ancestor = find_common_ancestor(root.right, values)

    if left_ancestor and right_ancestor:
        return root

    return left_ancestor or right_ancestor

def find_ancestor_of_leaf(root, target_value):
    if root is None:
        return None

    if root.value == target_value:
        return None  # La hoja misma no tiene ancestro

    if (root.left and root.left.value == target_value) or (root.right and root.right.value == target_value):
        return root

    left_ancestor = find_ancestor_of_leaf(root.left, target_value)
    right_ancestor = find_ancestor_of_leaf(root.right, target_value)

    return left_ancestor if left_ancestor else right_ancestor

def main():
    num_values = int(input("Ingrese la cantidad de valores que desea buscar: "))
    values = []

    for i in range(num_values):
        value = input(f"Ingrese el valor del nodo {i + 1}: ")
        values.append(value)

    common_ancestor = find_common_ancestor(root, values)

    if common_ancestor and common_ancestor.value in values:
        common_ancestor = find_ancestor_of_leaf(root, common_ancestor.value)

    if common_ancestor:
        print(f"El ancestro común de {', '.join(values)} es {common_ancestor.value}.")
    else:
        print(f"No se encontró un ancestro común para {', '.join(values)}.")

if __name__ == "__main__":
    main()