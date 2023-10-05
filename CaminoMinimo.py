import tkinter as tk
from tkinter import simpledialog

# Función para imprimir el itinerario en una etiqueta de Tkinter
def print_itinerary_to_label(dictionary, src, label):
    dest = dictionary.get(src)
    if not dest:
        return
    label.config(text=label.cget("text") + f'{src} --> {dest}\n')
    print_itinerary_to_label(dictionary, dest, label)

# Función para encontrar el itinerario mínimo
def finditinerary(tickets, label):
    destinations = {*tickets.values()}
    for k, v in tickets.items():
        if k not in destinations:
            print_itinerary_to_label(tickets, k, label)
            return

if __name__ == '__main__':
    # Preguntar al usuario cuántos trayectos va a recorrer
    num_trayectos = simpledialog.askinteger("Número de Trayectos", "¿Cuántos trayectos va a recorrer?")
    
    if num_trayectos is None or num_trayectos <= 0:
        exit()

    tickets = {}
    for i in range(num_trayectos):
        origen = simpledialog.askstring("Origen", f"Origen del trayecto {i + 1}:")
        destino = simpledialog.askstring("Destino", f"Destino del trayecto {i + 1}:")
        tickets[origen] = destino

    # Crear una ventana de Tkinter
    root = tk.Tk()
    root.title("Itinerario")

    # Crear una etiqueta para mostrar el itinerario
    itinerary_label = tk.Label(root, text="Itinerario:\n")
    itinerary_label.pack()

    # Encontrar y mostrar el itinerario en la etiqueta
    finditinerary(tickets, itinerary_label)

    # Iniciar el bucle principal de Tkinter
    root.mainloop()