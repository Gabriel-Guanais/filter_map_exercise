from functools import reduce

name_list =['pedro', 'guanais', 'catapora']
sum_letter = list(map(len, name_list))

answer = reduce(lambda x,y: x+y, sum_letter)
print(answer)