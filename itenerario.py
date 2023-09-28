def print_itinerary(dictionary, src):
    dest = dictionary.get(src)
    if not dest:
        return
    print(src + '-->' + dest)
    print_itinerary(dictionary, dest)

def finditinerary(tickets):
    destinations = {*tickets.values()}
    for k, v in tickets.items():
        if k not in destinations:
            print_itinerary(tickets, k)
            return

if __name__ == '__main__':
    tickets = {
        'LAX': 'DXB',
        'DFW': 'JFK',
        'LHR': 'DFW',
        'JFK': 'LAX'
    }
    finditinerary(tickets)