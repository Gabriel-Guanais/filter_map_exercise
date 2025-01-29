
def convert_odd_even (numbers):
    
    odd = list(filter(lambda x: x % 2 != 0, numbers))
    even = list(filter(lambda x: x % 2 == 0, numbers))
    
    odd_even_dic = {"Odd": odd, "Even":even}
    return odd_even_dic
      
nubers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
answer = convert_odd_even(nubers_list)

print(answer)
