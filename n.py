import numpy as np

# Definición de la función que implementa el algoritmo Neighbor-Joining
def neighbor_joining(D, taxa):
    n = len(taxa)
    
    # Caso base: si solo quedan 2 taxones, retornar el árbol
    if n == 2:
        tree = {}
        tree[taxa[0]] = {taxa[1]: D[0, 1]}
        tree[taxa[1]] = {taxa[0]: D[0, 1]}
        return tree, D

    total_distance = np.sum(D, axis=1)
    Q = np.zeros((n, n))

    for i in range(n):
        for j in range(i + 1, n):
            # Cálculo de la matriz Q
            Q[i, j] = (n - 2) * D[i, j] - total_distance[i] - total_distance[j]
            Q[j, i] = Q[i, j]

    min_Q = np.min(Q)
    i, j = np.unravel_index(np.argmin(Q), Q.shape)

    delta = (total_distance[i] - total_distance[j]) / (n - 2)
    limb_length_i = 0.5 * (D[i, j] + delta)
    limb_length_j = 0.5 * (D[i, j] - delta)

    new_taxon = f"({taxa[i]}:{limb_length_i},{taxa[j]}:{limb_length_j})"
    new_D = np.zeros((n - 1, n - 1))
    new_taxa = taxa[:i] + [new_taxon] + taxa[i+1:j] + taxa[j+1:]

    for k in range(i):
        new_D[i, k] = 0.5 * (D[i, k] + D[i, j] - D[j, k])
        new_D[k, i] = new_D[i, k]
        new_D[j, k] = 0.5 * (D[j, k] + D[i, j] - D[i, k])
        new_D[k, j] = new_D[j, k]

    for k in range(i+1, j):
        new_D[i, k] = 0.5 * (D[i, k] + D[i, j] - D[j, k])
        new_D[k, i] = new_D[i, k]
        new_D[j, k] = 0.5 * (D[j, k] + D[i, j] - D[i, k])
        new_D[k, j] = new_D[j, k]

    for k in range(j+1, n):
        new_D[i, k] = 0.5 * (D[i, k] + D[i, j] - D[j, k])
        new_D[k, i] = new_D[i, k]
        new_D[j, k] = 0.5 * (D[j, k] + D[i, j] - D[i, k])
        new_D[k, j] = new_D[j, k]

    new_D[:i, :j] = D[:i, :j]
    new_D[:i, j:] = D[:i, j+1:]
    new_D[i:, :j] = D[i+1:, :j]
    new_D[i:, j:] = D[i+1:, j+1:]

    # Recursivamente llamar a neighbor_joining con la nueva matriz de distancia y taxones
    subtree, distances = neighbor_joining(new_D, new_taxa)

    for k in range(n):
        if k != i and k != j:
            # Actualizar las distancias
            distances[new_taxon] = {}
            distances[new_taxon][new_taxa[k]] = 0.5 * (D[i, k] + D[i, j] - D[j, k])
            distances[new_taxa[k]] = {new_taxon: distances[new_taxon][new_taxa[k]]}

    del distances[taxa[i]]
    del distances[taxa[j]]

    return subtree, distances

# Pedir al usuario ingresar los taxones
taxa_list = input("Ingrese los taxones separados por comas (por ejemplo, A,B,C): ").split(',')
n = len(taxa_list)

# Pedir al usuario ingresar la matriz de distancia
print("Ingrese la matriz de distancia (separando las distancias por comas y las filas por saltos de línea):")
dist_matrix = []
for i in range(n):
    row = input().split(',')
    dist_matrix.append([float(x) for x in row])

# Convertir la lista en una matriz de distancia
dist_matrix = np.array(dist_matrix)

# Llamar a la función neighbor_joining para obtener el árbol filogenético y distancias
phylogenetic_tree, distances = neighbor_joining(dist_matrix, taxa_list)

# Imprimir el árbol filogenético
print("Árbol Filogenético:")
print(phylogenetic_tree)
# Imprimir las distancias de todos los taxones
print("Distancias entre Taxones:")
print(distances)
