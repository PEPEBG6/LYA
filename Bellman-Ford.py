import sys

# Una clase para representar un objeto graph
class Graph:
    # Constructor
    def __init__(self, edges, n):
        # Una lista de listas para representar una lista de adyacencia
        self.adjList = [[] for _ in range(n)]

        # Agregar bordes al grafo dirigido
        for (source, dest, weight) in edges:
            self.adjList[source].append((dest, weight))

    # Realizar DFS en el grafo y establecer la hora de salida de todos
    # los vértices del grafo
    def DFS(self, v, discovered, departure, time):
        # Marcar el nodo actual como descubierto
        discovered[v] = True

        # Hacer para cada arista (v, u)
        for (u, w) in self.adjList[v]:
            if not discovered[u]:
                time = self.DFS(u, discovered, departure, time)
        
        # Establecer la hora de salida para el nodo actual
        departure[time] = v
        time += 1
        return time

    def findLongestDistance(self, source, n):
        departure = [-1] * n
        discovered = [False] * n
        time = 0

        # Realizar el DFS en todos los vértices no descubiertos
        for i in range(n):
            if not discovered[i]:
                time = self.DFS(i, discovered, departure, time)

        cost = [sys.maxsize] * n
        cost[source] = 0

        for i in reversed(range(n)):
            v = departure[i]

            for (u, w) in self.adjList[v]:
                w = -w
                if cost[v] != sys.maxsize and cost[v] + w < cost[u]:
                    cost[u] = cost[v] + w

        for i in range(n):
            print(f'dist({source},{i}) = {-cost[i]}')

if __name__ == '__main__':
    edges = [
        (0, 6, 2), (1, 2, -4), (1, 4, 1), (1, 6, 8), (3, 0, 3),
        (3, 4, 5), (5, 1, 2), (7, 0, 6), (7, 1, -1), (7, 3, 4), (7, 5, -4)
    ]

    n = 8
    graph = Graph(edges, n)
    source = 7
    graph.findLongestDistance(source, n)
