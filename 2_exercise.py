# 2. Filtrar números pares de uma lista (com filter)

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9,]

def peer(number):
    if number % 2 == 0:
        return number

peer_filter = list(filter(peer, numbers_list))
print(peer_filter)
