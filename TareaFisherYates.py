import tkinter as tk
import random

# Definir una función para mezclar las cartas usando el algoritmo Fisher-Yates
def shuffle_deck():
    global deck
    deck = [f"{rank} DE {suit}" for suit in suits for rank in ranks]
    random.shuffle(deck)

# Definir una función para repartir cartas a los jugadores
def deal_cards():
    global deck
    num_players = int(player_entry.get())
    players = [[] for _ in range(num_players)]

    for _ in range(7):
        for player in players:
            card = deck.pop()
            player.append(card)

    for player_index, player_hand in enumerate(players):
        result_label.config(state=tk.NORMAL)
        result_label.insert(tk.END, f"Jugador {player_index + 1}: {', '.join(player_hand)}\n")
        result_label.see(tk.END)
        result_label.config(state=tk.DISABLED)

    if deck:
        next_card = deck.pop()
        next_card_label.config(text=f"Carta siguiente: {next_card}")
    else:
        next_card_label.config(text="No quedan más cartas en el mazo.")

# Crear la ventana principal
root = tk.Tk()
root.title("Mezclador de Cartas")

# Definir los valores de las cartas
suits = ["CORAZONES", "DIAMANTE", "PICAS", "TREBOL"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "JOTA", "REYNA", "REY", "A'S"]

# Mezclar las cartas
shuffle_deck()

# Crear etiquetas y entrada de texto
player_label = tk.Label(root, text="Número de Jugadores:")
player_label.pack()
player_entry = tk.Entry(root)
player_entry.pack()

deal_button = tk.Button(root, text="Repartir Cartas", command=deal_cards)
deal_button.pack()

result_label = tk.Text(root, height=20, width=40, state=tk.DISABLED)
result_label.pack()

next_card_label = tk.Label(root, text="", wraplength=200)
next_card_label.pack()

root.mainloop()