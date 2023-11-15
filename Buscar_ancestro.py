class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Crear el árbol con nodos predefinidos
root = TreeNode("Zeuz")
root.left = TreeNode("Apolo") 
root.left.right = TreeNode("Orfeo") 
root.left.right.left = TreeNode("Linus") 
root.left.right.right = TreeNode("Eurydice") 
root.left.right.right.left = TreeNode("Gargareia") 
root.left.right.right.left.left = TreeNode("Licaon") 
root.left.right.right.left.left.left = TreeNode("Nicomaco") 
root.left.right.right.left.left.left.left = TreeNode("Alcmeon") 
root.left.right.right.left.left.left.right = TreeNode("Astianacte") 
root.left.right.right.left.left.right = TreeNode("Misipe") 
root.left.right.right.left.left.right.left = TreeNode("Anaxibia") 
root.left.right.right.left.left.right.right = TreeNode("Semele") 
root.left.right.right.left.right = TreeNode("Cecropia") 
root.left.right.right.left.right.left = TreeNode("Erecteo") 
root.left.right.right.left.right.left.left = TreeNode("Aglaturo") 
root.left.right.right.left.right.left.left.left = TreeNode("Crecrops") 
root.left.right.right.left.right.left.left.right = TreeNode("Erysichthon") 
root.left.right.right.left.right.left.right = TreeNode("Herse") 
root.left.right.right.left.right.right = TreeNode("Atenea") 
root.left.right.right.left.right.right.left = TreeNode("Pandion") 
root.left.right.right.left.right.right.left.left = TreeNode("Egeo") 
root.left.right.right.left.right.right.left.right = TreeNode("Pallas") 
root.left.right.right.right = TreeNode("Argonautas") 
root.left.right.right.right.left = TreeNode("Cánace") 
root.left.right.right.right.left.left = TreeNode("Linceo") 
root.left.right.right.right.left.left.left = TreeNode("Euricione") 
root.left.right.right.right.left.right = TreeNode("Abante") 
root.left.right.right.right.left.right.left = TreeNode("Pero") 
root.left.right.right.right.left.right.right = TreeNode("Laodice") 
root.left.right.right.right.right = TreeNode("Estinfalo") 
root.left.right.right.right.right.left = TreeNode("Atys") 
root.left.right.right.right.right.left.left = TreeNode("Aglaura") 
root.left.right.right.right.right.left.right = TreeNode("Agile") 
root.left.right.right.right.right.right = TreeNode("Milon") 
root.left.right.right.right.right.right.left = TreeNode("Deifobo") 
root.left.right.right.right.right.right.right = TreeNode("Pródico") 
root.left.left = TreeNode("Asclepio")
root.left.left.left = TreeNode("Machaon")
root.left.left.left.right = TreeNode("Nicomedes")
root.left.left.left.right.left = TreeNode("Linanto")
root.left.left.left.right.left.left = TreeNode("Aleimon")
root.left.left.left.right.left.left.left = TreeNode("Pilos")
root.left.left.left.right.left.left.right = TreeNode("Argeo")
root.left.left.left.right.left.right = TreeNode("Acestor")
root.left.left.left.right.left.right.left = TreeNode("Poeas")
root.left.left.left.right.left.right.left.left = TreeNode("Philammon")
root.left.left.left.right.left.right.left.right = TreeNode("Sarpedon")
root.left.left.left.right.left.right.right = TreeNode("Piritoo")
root.left.left.left.right.left.right.right.left = TreeNode("Polidoro")
root.left.left.left.right.left.right.right.left.left = TreeNode("Peonio")
root.left.left.left.right.left.right.right.left.left.left = TreeNode("Anficlea")
root.left.left.left.right.left.right.right.left.left.left.left = TreeNode("Bato")
root.left.left.left.right.left.right.right.left.left.right = TreeNode("Icario")
root.left.left.left.right.left.right.right.left.left.right.left = TreeNode("Ersinoe")
root.left.left.left.right.left.right.right.left.left.right.left.left = TreeNode("Butes")
root.left.left.left.right.left.right.right.left.left.right.left.right = TreeNode("Crenaeus")
root.left.left.left.right.left.right.right.left.left.right.right = TreeNode("Ritmo")
root.left.left.left.right.left.right.right.left.left.right.right.left = TreeNode("Tirreno")
root.left.left.left.right.left.right.right.left.left.right.right.right = TreeNode("Carme")
root.left.left.left.right.left.right.right.left.right = TreeNode("Polifonte")
root.left.left.left.right.left.right.right.left.right.left = TreeNode("Bacis")
root.left.left.left.right.left.right.right.left.right.left.left = TreeNode("Cleoboa")
root.left.left.left.right.left.right.right.left.right.left.left.left = TreeNode("Clytie")
root.left.left.left.right.left.right.right.left.right.left.left.right = TreeNode("Leucothea")
root.left.left.left.right.left.right.right.left.right.left.right = TreeNode("Ismaro")
root.left.left.left.right.left.right.right.left.right.left.right.left = TreeNode("Marpessa")
root.left.left.left.right.left.right.right.left.right.left.right.right = TreeNode("Hypsipyle")
root.left.left.left.right.left.right.right.left.right.left = TreeNode("Cometes")
root.left.left.left.right.left.right.right.left.right.left.left = TreeNode("Lelanto")
root.left.left.left.right.left.right.right.left.right.left.left.left = TreeNode("Pegasides")
root.left.left.left.right.left.right.right.left.right.left.left.right = TreeNode("Nereides")
root.left.left.left.right.left.right.right.left.right.left.right = TreeNode("Titono")
root.left.left.left.right.left.right.right.left.right.left.right.left = TreeNode("Eos")
root.left.left.left.right.left.right.right.left.right.left.right.right = TreeNode("Hemera")
root.left.left.left.right.left.right.right.right = TreeNode("Cleopatra")
root.left.left.left.right.right = TreeNode("Medonte")
root.left.left.left.right.right.left = TreeNode("Lago")
root.left.left.left.right.right.left.left = TreeNode("Clitio")
root.left.left.left.right.right.left.right = TreeNode("Perieres")
root.left.left.left.right.right.right = TreeNode("Capaneo")
root.left.left.left.right.right.right.left = TreeNode("Licofonte")
root.left.left.left.right.right.right.right = TreeNode("Ilares")
root.left.left.left.left = TreeNode("Nireo")
root.left.left.left.left.right = TreeNode("Pandaro")
root.left.left.left.left.right.left = TreeNode("Atymnius")
root.left.left.left.left.right.left.left = TreeNode("Aglao")
root.left.left.left.left.right.left.left.left = TreeNode("Lilaea")
root.left.left.left.left.right.left.left.right = TreeNode("Podargos")
root.left.left.left.left.right.left.right = TreeNode("Androgea")
root.left.left.left.left.right.left.right.left = TreeNode("Ceneo")
root.left.left.left.left.right.left.right.right = TreeNode("Glanis")
root.left.left.left.left.right.right = TreeNode("Equeclea")
root.left.left.left.left.right.right.left = TreeNode("Ergino")
root.left.left.left.left.right.right.left.left = TreeNode("Corinna")
root.left.left.left.left.right.right.left.right = TreeNode("Hipaso")
root.left.left.left.left.right.right.right = TreeNode("Periboea")
root.left.left.left.left.right.right.right.left = TreeNode("Oeneus")
root.left.left.left.left.right.right.right.right = TreeNode("Agrius")
root.left.left.left.left.left = TreeNode("Iofante")
root.left.left.left.left.left.right = TreeNode("Ceafix")
root.left.left.left.left.left.right.left = TreeNode("Toloso")
root.left.left.left.left.left.right.left.left = TreeNode("Gelone")
root.left.left.left.left.left.right.left.right = TreeNode("Batis")
root.left.left.left.left.left.right.right = TreeNode("Cerope")
root.left.left.left.left.left.right.right.left = TreeNode("Europa")
root.left.left.left.left.left.right.right.right = TreeNode("Cadmus")
root.left.left.left.left.left.left = TreeNode("Sicino")
root.left.left.left.left.left.left.right = TreeNode("Sibaris")
root.left.left.left.left.left.left.right.left = TreeNode("Hesperia")
root.left.left.left.left.left.left.right.right = TreeNode("Lapyx")
root.left.left.left.left.left.left.left = TreeNode("Etolo")
root.left.left.left.left.left.left.left.right = TreeNode("Thestius")
root.left.left.left.left.left.left.left.left = TreeNode("Leucippe")
root.right=TreeNode("Artemisa")
root.right.right=TreeNode("Callisto")
root.right.right.right=TreeNode("Iasion")
root.right.right.right.right=TreeNode("Pluto")
root.right.right.right.right.right=TreeNode("Iaco")
root.right.right.right.right.right.left=TreeNode("Acasto")
root.right.right.right.right.left=TreeNode("Zagreo")
root.right.right.right.right.left.left=TreeNode("Agave")
root.right.right.right.right.left.left.left=TreeNode("Penteo")
root.right.right.right.right.left.left.right=TreeNode("Pirante")
root.right.right.right.right.left.right=TreeNode("Pantino")
root.right.right.right.right.left.right.left=TreeNode("Menesicle")
root.right.right.right.right.left.right.right=TreeNode("Leocoridas")
root.right.right.right.left=TreeNode("Demofonte")
root.right.right.right.left.left=TreeNode("amintor")
root.right.right.right.left.right=TreeNode("Cale")
root.right.right.right.left.left.left=TreeNode("Emetes")
root.right.right.right.left.left.right=TreeNode("Estesicoro")
root.right.right.right.left.right.left=TreeNode("Micceon")
root.right.right.right.left.right.right=TreeNode("Lutro")
root.right.right.right.left.left.left.left=TreeNode("Psamathe")
root.right.right.right.left.left.left.right=TreeNode("Echinades")
root.right.right.right.left.left.right.left=TreeNode("Arete")
root.right.right.right.left.left.right.right=TreeNode("Nicias")
root.right.right.right.left.right.left.left=TreeNode("Hipseo")
root.right.right.right.left.right.left.right=TreeNode("Sceus")
root.right.right.right.left.right.right.left=TreeNode("Himera")
root.right.right.right.left.right.right.right=TreeNode("Eryx")
root.right.right.left=TreeNode("Arcas")
root.right.right.left.left=TreeNode("Elato")
root.right.right.left.right=TreeNode("Azeo")
root.right.right.left.left.left=TreeNode("Apolis")
root.right.right.left.right.left=TreeNode("Carpo")
root.right.right.left.right.right=TreeNode("Eufrosine")
root.right.right.left.right.left.left=TreeNode("Ascaio")
root.right.right.left.right.left.right=TreeNode("Corinto")
root.right.right.left.right.right.left=TreeNode("Cleta")
root.right.right.left.right.right.right=TreeNode("Euforion")
root.right.right.left.right.left.left.left=TreeNode("Ateneo")
root.right.right.left.right.left.left.right=TreeNode("Autoctona")
root.right.right.left.right.left.right.left=TreeNode("Eunostos")
root.right.right.left.right.left.right.right=TreeNode("Bellerofonte")
root.right.right.left.right.right.left.left=TreeNode("Doris")
root.right.right.left.right.right.left.right=TreeNode("Melite")
root.right.right.left.right.right.right.left=TreeNode("Deifone")
root.right.right.left.right.right.right.right=TreeNode("Danae")
root.right.left = TreeNode("Hermes")
root.right.left.left = TreeNode("Pan")
root.right.left.left.left = TreeNode("Silenos")
root.right.left.left.left.left = TreeNode("Fauno")
root.right.left.left.left.left.left = TreeNode("Latinus")
root.right.left.left.left.left.left.left = TreeNode("Silvius")
root.right.left.left.left.left.left.right = TreeNode("Aventino")
root.right.left.left.left.left.right = TreeNode("Tarquino")
root.right.left.left.left.left.right.left = TreeNode("Arúntio")
root.right.left.left.left.left.right.right = TreeNode("Tanaquil")
root.right.left.left.left.right = TreeNode("Marone")
root.right.left.left.left.right.left = TreeNode("Sileno")
root.right.left.left.left.right.left.left = TreeNode("Filira")
root.right.left.left.left.right.left.right = TreeNode("Pegaso")
root.right.left.left.right = TreeNode("Eufeme")
root.right.left.left.right.left = TreeNode("Batus")
root.right.left.left.right.left.left = TreeNode("Elatiades")
root.right.left.left.right.left.left.left = TreeNode("Ameinias")
root.right.left.left.right.left.left.right = TreeNode("Molon")
root.right.left.left.right.left.right = TreeNode("Epeio")
root.right.left.left.right.left.right.left = TreeNode("Endeo")
root.right.left.left.right.right = TreeNode("Eurinome")
root.right.left.left.right.right.left = TreeNode("Lacedemon")
root.right.left.left.right.right.left.left = TreeNode("Dorio")
root.right.left.left.right.right.left.right = TreeNode("Eurice")
root.right.left.left.right.right.right = TreeNode("Gala")
root.right.left.left.right.right.right.left = TreeNode("Alexiada")
root.right.left.left.right.right.right.right = TreeNode("Polydora")
root.right.left.right = TreeNode("Dionisio")
root.right.left.right.left = TreeNode("Priapo")
root.right.left.right.left.left = TreeNode("Adono")
root.right.left.right.left.left.left = TreeNode("Ninias")
root.right.left.right.left.left.left.left = TreeNode("Cuidir")
root.right.left.right.left.left.left.right = TreeNode("Polyxeño")
root.right.left.right.left.left.right = TreeNode("Agdistis")
root.right.left.right.left.left.right.left = TreeNode("Circe")
root.right.left.right.left.left.right.right = TreeNode("Acis")
root.right.left.right.left.right = TreeNode("Cefiro")
root.right.left.right.left.left.left = TreeNode("Balio")
root.right.left.right.left.left.left.left = TreeNode("Jocasta")
root.right.left.right.left.left.left.right = TreeNode("Harmonia")
root.right.left.right.left.left.right = TreeNode("Xanto")
root.right.left.right.left.left.right.left = TreeNode("Antigona")
root.right.left.right.left.left.right.right = TreeNode("Ismene")
root.right.left.right.right = TreeNode("Ampleo")
root.right.left.right.right.left = TreeNode("Bromio")
root.right.left.right.right.left.left = TreeNode("Liriope")
root.right.left.right.right.left.left.left = TreeNode("Narciso")
root.right.left.right.right.left.left.right = TreeNode("Melo")
root.right.left.right.right.left.right = TreeNode("Naso")
root.right.left.right.right.right = TreeNode("Oinopion")
root.right.left.right.right.right.left = TreeNode("Ampelo")
root.right.left.right.right.right.left.left = TreeNode("Linea")
root.right.left.right.right.right.left.right = TreeNode("Calcone")
root.right.left.right.right.right.right = TreeNode("Tiro")
root.right.left.right.right.right.right.left = TreeNode("Neleo")
root.right.left.right.right.right.right.right = TreeNode("Pelias")


def find_common_ancestor(root, values):
     # Encuentra el ancestro común más cercano de una lista de valores de nodos en el árbol.
    if root is None:
        return None

    if root.value in values:
         # Si el valor del nodo actual está en la lista de valores, es un ancestro.
        return root  

    # Busca en los subárboles izquierdo y derecho.
    left_ancestor = find_common_ancestor(root.left, values)
    right_ancestor = find_common_ancestor(root.right, values)

    if left_ancestor and right_ancestor:
        # Si se encuentra en ambos subárboles, este nodo es el ancestro común.
        return root

    return left_ancestor or right_ancestor

def find_ancestor_of_leaf(root, target_value):
     # Encuentra el ancestro de una hoja específica en el árbol.
    if root is None:
        return None

    if root.value == target_value:
        return None  

    if (root.left and root.left.value == target_value) or (root.right and root.right.value == target_value):
        return root

    left_ancestor = find_ancestor_of_leaf(root.left, target_value)
    right_ancestor = find_ancestor_of_leaf(root.right, target_value)

    return left_ancestor if left_ancestor else right_ancestor

# Función para verificar si un nodo es el padre de todos los valores dados
def is_parent_of_all(root, values):
    if root is None:
        return False
    
    # Contar cuántos valores se encuentran en el subárbol del nodo
    count = 0
    stack = [root]
    while stack:
        node = stack.pop()
        if node.value in values:
            count += 1
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    
    
    return count == len(values)

def main():
    num_values = int(input("Ingrese la cantidad de Nombres que desea buscar: "))
    values = []

    for i in range(num_values):
        value = input(f"Ingrese el valor del nodo {i + 1}: ")
        values.append(value)

    common_ancestor = find_common_ancestor(root, values)

    # Verificar si el ancestro común es el padre de todos los valores
    if is_parent_of_all(common_ancestor, values):
        # Verificar si el ancestro común es uno de los valores dados
        if common_ancestor.value in values:
            
            common_ancestor = find_ancestor_of_leaf(root, common_ancestor.value)
        
    else:
        
        common_ancestor = None

    if common_ancestor:
        print(f"El ancestro común de {', '.join(values)} es {common_ancestor.value}.")
    else:
        print(f"No se encontró un ancestro común para {', '.join(values)}.")

if __name__ == "__main__":
    main()