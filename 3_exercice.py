from functools import reduce

number_list = [1, 2, 3, 4, 5, 6,]
sum_nubers = reduce(lambda x, y: x + y, number_list)

print(sum_nubers)