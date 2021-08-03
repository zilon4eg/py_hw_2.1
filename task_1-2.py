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

def get_shop_list_by_dish(cook_book, dish, person_count):
    dict_ingredients_count_dict = {}
    for ingredients in cook_book[dish]:
        ingredients_count_dict = {}
        ingredients_count_dict['measure'] = ingredients['measure']
        ingredients_count_dict['quantity'] = int(ingredients['quantity']) * person_count
        dict_ingredients_count_dict[ingredients['ingredient_name']] = ingredients_count_dict
    return dict_ingredients_count_dict

def get_shop_list_by_dishes(dishes, person_count):
    shop_list_by_dishes = {}
    cook_book = add_list_ingredient_to_cook_book('recipes.txt')
    shop_list_by_dishes = {}
    for dish in dishes:
        shop_list_by_dishes.update(get_shop_list_by_dish(cook_book, dish, person_count))
    return shop_list_by_dishes

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

# print(add_list_ingredient_to_cook_book('recipes.txt'))