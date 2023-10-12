#Una clase para representar un objeto grafo
class Graph:
    #constructor
    def __init__(self, edges, n):
        #Una lista de listas para representar una lista de adyacencia
        self.adjList = [[] for _ in range(n)]
        #Agregar bordes al grafo no dirigido
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

#Función para comprobar si es seguro asignar el colo 'c' al vertice 'v'
def isSafe(graph, color, v, c):
    #Verifica el color de cada vertice adyacente de 'v'
    for u in graph.adjList[v]:
        if color[u] == c:
            return False
    return True

def kColoreable(g, color, k, v, n):
    
    if v == n:
        print([COLORS[color[v]] for v in range(n)])
        return
            
    # prueba todas las combinaciones posibles de colores disponibles
    for c in range (1, k+1):
       
        if isSafe(g, color, v, c):
            color[v] = c
            
            kColoreable(g, color, k, v+1, n)
           
            color[v] = 0

def ingresar_borde():
    print("Ingrese el primer nodo (X): ")
    a = int(input())
    print("Ingrese el segundo nodo (Y): ")
    b = int(input())
    return (a, b)



if __name__ =='__main__':
    
    edges = []

    print("Cuantos colores: ")
    k = int(input())

    print("Cuantos nodos o vértices: ")
    n = int(input())

    print("Cuantas aristas: ")
    v = int(input())

    edges = []

    for i in range(v):
        edges.append(ingresar_borde())

    #Lista de colores
    COLORS = ['Azul', 'Celeste', 'Dorado', 'Café', 'Naranja', 'Verde', 'Blanco', 'Gris', 'Negro', 'Morado']
    
    #Crear un grafo a partir de una lista de bordes
    g = Graph(edges, n) 
    
    color = [None] * n

    print("Matriz de colores: ")
    #Imprime todas las k-configuraciones coloreables del graph
    kColoreable(g, color, k, 0, n)
