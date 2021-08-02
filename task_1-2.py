import os

def list_to_dict_ingredient(list_ingredient):
    count = 0
    list_key = ['ingredient_name', 'quantity', 'measure']
    dict_ingredient = {}
    while count != 3:
        dict_ingredient[list_key[count]] = list_ingredient[count]
        count += 1
    return dict_ingredient

def add_ingredient_to_list(count_string_ingredient, file):
    count = 0
    list_cook_book = []
    while count != count_string_ingredient:
        list_ingredient = str(file.readline().strip())
        list_ingredient = list_ingredient.split(' | ')
        dict_ingredient = list_to_dict_ingredient(list_ingredient)
        count += 1
        list_cook_book.append(dict_ingredient)
    return list_cook_book

def add_list_ingredient_to_cook_book(file_name):
    cook_book = {}
    with open(os.path.join(os.getcwd(), file_name), encoding='utf-8') as file:
        for line in file:
            dish = str(line.strip())
            count_string_ingredient = int(file.readline().strip())
            cook_book[dish] = add_ingredient_to_list(count_string_ingredient, file)
            file.readline()
    return cook_book



print(add_list_ingredient_to_cook_book('recipes.txt'))