# Question 1
import math

def calculate_area(shape, x, y=0):
    if shape == 't':
        return 0.5 * x * y
    elif shape == 'r':
        return x * y
    elif shape == 's':
        return x * x
    elif shape == 'c':
        return math.pi * (x ** 2)
    else:
        return "Invalid shape"

# Question 2

def locate_letter(sentence, letter):
    indices = []
    
    for index, char in enumerate(sentence):
        if char == letter:
            indices.append(index)
    
    return indices

# Question 3

def multiplication_table(n):
    table = []

    for i in range(1, n + 1):
        sub_list = [i * j for j in range(1, i + 1)]
        table.append(sub_list)
    
    return table

# Bonus 

def dictionary(names):
    name_dict = {}

    for name in names:
        first_letter = name[0]
    
        if first_letter in name_dict:
            name_dict[first_letter].append(name)
        else:
            name_dict[first_letter] = [name]

    return name_dict

