import numpy as np

# Definición de la función Neighbor Joining 
def neighbor_joining(D):
    n = len(D)
    
    # Comprobación: Si solo hay 2 elementos, creamos un árbol con una sola rama y lo devolvemos
    if n == 2:
        T = {0: {1: D[0][1]}}
        return T

    # Función anónima para calcular la suma de las distancias de una fila
    total_distance = lambda i: sum(D[i])
    
    # Inicialización de la matriz Q con ceros
    Q = np.zeros((n, n))
    
    # Cálculo de la matriz Q según la fórmula del algoritmo Neighbor Joining
    for i in range(n):
        for j in range(n):
            if i != j:
                Q[i][j] = (n - 2) * D[i][j] - total_distance(i) - total_distance(j)

    # Encontrar el mínimo valor en la matriz Q
    min_Q = np.argmin(Q)
    i, j = divmod(min_Q, n)
    
    # Cálculo de delta y las longitudes de las ramas para los nodos i y j
    delta = (total_distance(i) - total_distance(j)) / (n - 2)
    limb_length_i = 0.5 * (D[i][j] + delta)
    limb_length_j = 0.5 * (D[i][j] - delta)
    
    # Llamada recursiva de neighbor_joining con una matriz reducida (sin las filas i y j)
    T = neighbor_joining(remove_row_col(D, i, j))
    
    # Agregar las longitudes de las ramas para los nodos i y j al árbol
    T[i] = {n: limb_length_i}
    T[j] = {n: limb_length_j}
    
    # Calcular las longitudes de las ramas para los nodos restantes
    for k in range(n - 1):
        if k != i and k != j:
            D_kn = 0.5 * (D[k][i] + D[k][j] - D[i][j])
            T[k] = {n: D_kn, n: 0.5 * (D[i][j] + D[i][k] - D[j][k])}

    # Devolver el árbol filogenético construido
    return T

# Función para eliminar una fila y columna específicas de una matriz
def remove_row_col(matrix, row, col):
    matrix = np.delete(matrix, (row), axis=0)
    matrix = np.delete(matrix, (col), axis=1)
    return matrix

# Ejemplo de uso con una matriz de distancias
distance_matrix = np.array([
    [0, 5, 9, 9],
    [5, 0, 10, 10],
    [9, 10, 0, 8],
    [9, 10, 8, 0]
])

# Llamada a la función neighbor_joining para construir el árbol filogenético
tree = neighbor_joining(distance_matrix)

# Imprimir el árbol resultante
print(tree)
