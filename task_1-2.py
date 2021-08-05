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

def addition_of_dict(dict_1, dict_2):
    dict_result = dict_1
    for element_1 in dict_1:
        if element_1 in dict_1.keys() and element_1 in dict_2.keys():
            dict_2[element_1]['quantity'] = dict_2[element_1]['quantity'] + dict_1[element_1]['quantity']
    dict_result.update(dict_2)
    return dict_result

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = add_list_ingredient_to_cook_book('recipes.txt')
    shop_list_by_dishes = {}
    for dish in dishes:
        addition_of_dict(shop_list_by_dishes, get_shop_list_by_dish(cook_book, dish, person_count))
    return shop_list_by_dishes

def sorted_dict(dict):
    sorted_dict = {}
    sorted_keys = sorted(dict, key=dict.get)
    for key in sorted_keys:
        sorted_dict[key] = dict[key]
    return sorted_dict

def write_dict_in_file(dict, file_name):
    with open(os.path.join(os.getcwd(), file_name), 'a', encoding='utf-8') as file:
        for key in dict:
            file.write(f'{key}\n{dict[key][0]}\n{dict[key][1]}\n')

def find_and_add_file_in_dir(dir_name):
    list_dir = os.listdir(os.path.join(os.getcwd(), dir_name))
    print(list_dir)
    file_in_dir = {}
    for file_name in list_dir:
        with open(os.path.join(os.getcwd(), dir_name, file_name), encoding='utf-8') as file:
            text_in_file = str()
            for id, line in enumerate(file, 1):
                text_in_file += line
            file_in_dir[file_name] = id, text_in_file
    sorted_file_in_dir = sorted_dict(file_in_dir)
    write_dict_in_file(sorted_file_in_dir, 'sorted_result_file.txt')

#===(Формируем словарь на основании данных из файла)==
# print(add_list_ingredient_to_cook_book('recipes.txt'))

#===(Создаем список ингридиентов для заданных блюд по количеству персон)==
# print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

print(find_and_add_file_in_dir('data'))