from random import randrange

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def shuffle(A):
    for i in range(len(A) - 1):
        j = randrange(i, len(A))
        swap(A, i, j)

if __name__ == '__main__':
    # Crear un array vacío
    datos = []

    # Pedir al usuario la cantidad de datos que desea ingresar
    num_datos = int(input("Ingrese la cantidad de datos que desea agregar: "))

    # Pedir al usuario ingresar los datos uno por uno
    for i in range(num_datos):
        dato = int(input(f"Ingrese el dato {i + 1}: "))
        datos.append(dato)

    # Mezclar los datos aleatoriamente
    shuffle(datos)

    # Imprimir los datos aleatorios
    print("Datos aleatorios:")
    for dato in datos:
        print(dato)