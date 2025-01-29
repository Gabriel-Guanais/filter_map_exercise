# 2. Filtrar números pares de uma lista (com filter)

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9,]


peer_filter = list(filter(lambda x : x % 2 == 0, numbers_list))
print(peer_filter)
