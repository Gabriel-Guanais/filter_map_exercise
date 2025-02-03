
tuple_list = [(2, 8), (4, 5, 6), (1, 2)]

resultado = list(filter(lambda x: sum(x) / len(x) >= 5, tuple_list))

print(resultado)