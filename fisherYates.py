from random import randrange
import tkinter as tk

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def shuffle(A):
    for i in range(len(A) - 1):
        j = randrange(i, len(A))
        swap(A, i, j)

def ingresar_datos():
    datos = []
    num_datos = int(input("Ingrese la cantidad de datos que desea agregar: "))

    for i in range(num_datos):
        dato = int(input(f"Ingrese el dato {i + 1}: "))
        datos.append(dato)

    return datos

def mostrar_ventana(datos):
    ventana = tk.Tk()
    ventana.title("Datos Aleatorios")

    etiqueta = tk.Label(ventana, text="Datos aleatorios:")
    etiqueta.pack()

    for dato in datos:
        etiqueta_dato = tk.Label(ventana, text=str(dato))
        etiqueta_dato.pack()

    ventana.mainloop()

if __name__ == '__main__':
    datos = ingresar_datos()

    shuffle(datos)

    mostrar_ventana(datos)

