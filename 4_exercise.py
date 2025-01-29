# 4. Nomes com mais de 5 letras (com filter)

name_list = ['Pedro', 'Gabriel', 'Ana', 'Matheus']
    
    
    
letter_counter = list(filter(lambda x: len(x) > 5, name_list))
print(letter_counter)