import tkinter as tk

# Una clase para representar un conjunto disjunto
class DisjointSet:
    def __init__(self):
        self.parent = {}

    # Realiza la operación MakeSet
    def makeSet(self, n):
        # Crear 'n' conjuntos disjuntos (uno para cada vértice)
        for i in range(n):
            self.parent[i] = i

    # Encuentra la raíz del conjunto al que pertenece el elemento 'k'
    def find(self, k):
        if self.parent[k] == k:
            return k
        # Recurre para el padre hasta que encontramos la raíz
        return self.find(self.parent[k])

    # Realizar la unión de dos subconjuntos
    def union(self, a, b):
        # Encontrar la raíz de los conjuntos a los que pertenecen los elementos x e y
        x = self.find(a)
        y = self.find(b)

        self.parent[x] = y

# Función para construir MST usando el algoritmo de Kruskal
def runKruskalAlgorithm(edges, n):
    # Almacenar los bordes presentes en MST
    MST = []

    # Inicializa la clase 'DisjointSet'
    # Crea un conjunto singleton para cada elemento del universo
    ds = DisjointSet()
    ds.makeSet(n)

    index = 0

    # Ordena los bordes aumentando el peso
    edges.sort(key=lambda x: x[2])
    while len(MST) != n - 1:
        # Considerar el borde siguiente con peso mínimo del gráfico
        (src, dest, weight) = edges[index]
        index = index + 1

        # Encontrar la raíz de los conjuntos a los que se unen dos extremos
        # Vértices de la siguiente arista pertenecen
        x = ds.find(src)
        y = ds.find(dest)

        # Si ambos extremos tienen diferentes padres, pertenecen a
        # Diferentes componentes conectados y se pueden incluir en MST
        if x != y:
            MST.append((src, dest, weight))
            ds.union(x, y)

    return MST

def display_result():
    result_label.config(state=tk.NORMAL)
    result_label.delete('1.0', tk.END)
    
    # (u, v, w) el triplete representa un borde no dirigido desde
    # vértice 'u' a vértice con peso 'w'
    edges = [
        (1, 8, 10),
        (1, 2, 3),
        (1, 3, 5),
        (2, 1, 3),
        (2, 3, 5 ),
        (2, 5, 4 ),
        (2, 4, 6 ),
        (2, 7, 6),
        (2, 8, 6),
        (3, 1, 5),
        (3, 2, 5),
        (3, 5, 1),
        (3, 6, 7),
        (4, 1, 2),
        (4, 2, 6),
        (4, 5, 12),
        (4, 8, 14),
        (5, 2, 4),
        (5, 3, 1),
        (5, 4, 12),
        (5, 7, 15),
        (6, 3, 7),
        (6, 8, 9),
        (7, 2, 6),
        (7, 3, 9),
        (7, 5, 15),
        (7, 8, 3),
        (8, 1, 10),
        (8, 2, 6),
        (8, 4, 14),
        (8, 6, 9),
        (8, 7, 3)
    ]

    n = 16

    e = runKruskalAlgorithm(edges, n)

    for edge in e:
        result_label.insert(tk.END, f"({edge[0]}, {edge[1]}) - Peso: {edge[2]}\n")
    
    result_label.config(state=tk.DISABLED)

# Crear la ventana principal
root = tk.Tk()
root.title("Algoritmo de Kruskal")

# Botón para ejecutar el algoritmo y mostrar el resultado
run_button = tk.Button(root, text="Ejecutar Kruskal", command=display_result)
run_button.pack()

# Etiqueta para mostrar el resultado
result_label = tk.Text(root, height=20, width=40, state=tk.DISABLED)
result_label.pack()

# Iniciar la aplicación
root.mainloop()