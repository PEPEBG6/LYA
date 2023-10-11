# Una clase para representar un objeto graph
class Graph:
    # Constructor
    def __init__(self, edges, n):
        # una lista de listas para representar una lista de adyacencia
        self.adjList = [[] for _ in range(n)]
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

# Función para comprobar si es seguro asignar el color 'c' al vértice 'v'
def isSafe(graph, color, v, c):
    for u in graph.adjList[v]:
        if color[u] == c:
            return False
    return True

def kColorable(g, color, k, v, n):
    if v == n:
        print([COLORS[color[v]] for v in range(n)])
        return

    for c in range(1, k + 1):
        if isSafe(g, color, v, c):
            color[v] = c
            kColorable(g, color, k, v + 1, n)
            color[v] = 0

if __name__ == '__main__':
    k = int(input("Ingrese la cantidad de colores (k): "))  # Solicitar solo el número de colores

    # Lista de bordes de graph según el diagrama anterior
    edges = [(0, 1), (0, 3), (1, 2), (1, 3), (1, 4), (4, 5), (4, 6), (5, 3)]

    COLORS = ['Azul', 'Azul Claro', 'Verde', 'Verde','Rojo','Negro','Violeta','Morado', ]

    n = 6
    g = Graph(edges, n)
    color = [None] * n
    kColorable(g, color, k, 0, n)
