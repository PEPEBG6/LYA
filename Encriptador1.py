from tkinter import (Tk, Text, Button, Label, Menu, Entry,
                     END, INSERT, SEL_FIRST, SEL_LAST)

class GUI(Tk):
    "Interfaz Grafica..."

    def __init__(self):
        super(GUI,self).__init__()
        self.geometry("300x350+350+80")  # Increased height to accommodate the new entry widget
        self.title("Encriptador")
        self.resizable(width=False, height=False)

        try:
            self.iconbitmap("icono.ico")
        except:
            pass

        self.texto = Text(self, font=datos.fuente2)
        self.texto.place(x=0, y=30, width=300, height=218)

        self.panel = Label(self,
                           text="Ingrese un texto",
                           bg="gray93",
                           font=datos.fuente2)
        self.panel.place(x=0, y=0, width=300, height=30)

        self.botones()
        self.menu_desplegable()
        self.entry_capas()

    def botones(self):
        boton_encriptar = Button(self,
                                 text="Encriptar",
                                 font=datos.fuente2,
                                 relief="flat",
                                 command=lambda: funcion.boton("encriptado"))
        boton_encriptar.place(x=0, y=278, width=150, height=52)

    def menu_desplegable(self):
        self.menu_desplegable = Menu(self, tearoff=0)

        self.menu_desplegable.add_command(label="Cortar",
                                          font=datos.fuente,
                                          command=lambda: funcion.menu("cortar"))

        self.menu_desplegable.add_command(label="Copiar",
                                          font=datos.fuente,
                                          command=lambda: funcion.menu("copiar"))

        self.menu_desplegable.add_separator()

        self.menu_desplegable.add_command(label="Pegar",
                                          font=datos.fuente,
                                          command=lambda: funcion.menu("pegar"))

        self.texto.bind("<Button-3>", lambda evento: self.menu_desplegable.post(evento.x_root, evento.y_root))

    def entry_capas(self):
        self.entry_label = Label(self, text="Capas de encriptación:", font=datos.fuente2)
        self.entry_label.place(x=0, y=248, width=150, height=30)

        self.entry_capas = Entry(self, font=datos.fuente2)
        self.entry_capas.place(x=150, y=248, width=150, height=30)

class Funciones:
    "Conjunto de funciones..."

    def encriptado(self, mensaje, capas):
        # Método para encriptar con el número de capas especificado
        traduccion = mensaje
        for _ in range(capas):
            traduccion = self._encriptar_una_capa(traduccion)
        return traduccion

    def _encriptar_una_capa(self, mensaje):
        # Método para encriptar una capa
        clave = 2
        traduccion = ""
        for simbolo in mensaje:
            if simbolo.isalpha():
                num = ord(simbolo)
                num += clave
                if simbolo.isupper():
                    if num > ord("Z"):
                        num -= 26
                    elif num < ord("A"):
                        num += 26
                elif simbolo.islower():
                    if num > ord("z"):
                        num -= 26
                    elif num < ord("a"):
                        num += 26
                traduccion += chr(num)
            else:
                traduccion += simbolo
        return traduccion

    def boton(self, modo):
        mensaje = ventana.texto.get("0.0", END)
        capas = int(ventana.entry_capas.get())  # Get the number of layers from the entry widget
        texto = self.encriptado(mensaje, capas)
        ventana.texto.delete("0.0", END)
        ventana.texto.insert("0.0", texto)
        ventana.panel.config(text=f"Texto encriptado ({capas} capas)")

    def menu(self, modo):
        if modo == "cortar":
            try:
                ventana.texto.clipboard_clear()
                ventana.texto.clipboard_append(ventana.texto.selection_get())
                ventana.texto.delete(SEL_FIRST, SEL_LAST)
            except:
                print("Seleccion vacia")
        elif modo == "copiar":
            try:
                ventana.texto.clipboard_clear()
                ventana.texto.clipboard_append(ventana.texto.selection_get())
            except:
                print("Seleccion vacia")
        elif modo == "pegar":
            try:
                ventana.texto.insert(INSERT, ventana.texto.selection_get(selection="CLIPBOARD"))
            except:
                print("Seleccion vacia")

class datos:
    "Conjunto de variables usadas por el programa..."
    fuente = ("Century Gothic", 9)
    fuente2 = ("Century Gothic", 10)

if __name__ == "__main__":
    funcion = Funciones()
    ventana = GUI()
    ventana.mainloop()
