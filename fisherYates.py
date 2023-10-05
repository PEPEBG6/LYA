import tkinter as tk
from random import randrange

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def shuffle(A):
    for i in range(len(A) - 1):
        j = randrange(i, len(A))
        swap(A, i, j)

def solicitar_datos():
    ventana_solicitar = tk.Toplevel(ventana_principal)
    ventana_solicitar.title("Ingresar Datos")

    etiqueta_num_datos = tk.Label(ventana_solicitar, text="Ingrese la cantidad de datos:")
    etiqueta_num_datos.pack()

    entry_num_datos = tk.Entry(ventana_solicitar)
    entry_num_datos.pack()

    def ingresar_datos():
        num_datos = int(entry_num_datos.get())
        datos = []

        for i in range(num_datos):
            dato = int(input(f"Ingrese el dato {i + 1}: "))
            datos.append(dato)

        shuffle(datos)

        ventana_resultado = tk.Toplevel(ventana_principal)
        ventana_resultado.title("Datos Aleatorios")

        resultado = tk.Label(ventana_resultado, text="Datos aleatorios:\n" + ", ".join(map(str, datos)))
        resultado.pack()

    boton_ingresar = tk.Button(ventana_solicitar, text="Ingresar Datos", command=ingresar_datos)
    boton_ingresar.pack()

# Crear una ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Generador de Datos Aleatorios")

# Botón para solicitar datos
boton_solicitar = tk.Button(ventana_principal, text="Solicitar Datos", command=solicitar_datos)
boton_solicitar.pack()

# Iniciar el bucle principal de Tkinter
ventana_principal.mainloop()