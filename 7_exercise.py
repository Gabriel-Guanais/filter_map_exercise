def category_numbers(n):
    positive = list(filter(lambda x: x > 0, n))
    negative = list(filter(lambda x: x < 0, n))
    zero = list(filter(lambda x: x == 0, n))
    
    category_dic = {"Positive": positive, "Negative": negative, "Zero": zero}
    return category_dic

numbers_list = [1, -3, 0, 0, 2, -1, 3]
answer = category_numbers(numbers_list)
print(answer)