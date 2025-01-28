name_list = ['Pedro', 'Gabriel', 'Ana', 'Matheus']

    
    
letter_counter = list(filter(lambda x: len(x) > 5, name_list))
print(letter_counter)