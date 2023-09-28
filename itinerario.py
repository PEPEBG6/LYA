# Función para imprimir el itinerario
def print_itinerary(dictionary, src):
    dest = dictionary.get(src)
    if not dest:
        return
    print(src + ' --> ' + dest)
    print_itinerary(dictionary, dest)

# Función para encontrar el itinerario
def finditinerary(tickets):
    destinations = {*tickets.values()}
    for k, v in tickets.items():
        if k not in destinations:
            print_itinerary(tickets, k)
            return

if __name__ == '__main__':
    tickets = {
        'CONSTITUCION': 'ISABEL LA CATOLICA',
        'CHABACANO': 'NEZA',
        '4 CAMINOS': 'PUERTO AEREO',
        'PUERTO AEREO': 'T AUTOBUSES',
        'PINO SUAREZ': 'ZOCALO',
        'T AUTOBUSES': 'PINO SUAREZ',
        'ZOCALO': 'CHABACANO',
        'NEZA': 'CONSTITUCION'
    }
    finditinerary(tickets)