import os

def create_dict_from_file(file_name):
    """Функция фтения файла + создание словаря нужного формата"""
    file_path = os.path.abspath(os.path.join(file_name))
    cook_dict = {}
    with open(file_path, encoding='utf8') as file_work:
        for line in file_work:
            dish_name = line.lower().strip().capitalize()
            counter = int(file_work.readline())
            list_of_ingridient = []
            for i in range(counter):
                temp_dict = {}
                ingridient = file_work.readline().lower()
                ingridient = ingridient.strip().split('|')
                temp_dict['ingridient_name'] = ingridient[0].strip().capitalize()
                temp_dict['quantity'] = int(ingridient[1])
                temp_dict['measure'] = ingridient[2].strip().capitalize()
                list_of_ingridient.append(temp_dict)
            cook_dict[dish_name] = list_of_ingridient
            file_work.readline()
    return cook_dict


def get_shop_list_by_dishes(dishes, person_count, cook_book):
    print(dishes)
    shop_list = {}
    for dish in dishes:
        dish.capitalize()
        if dish in cook_book.keys():
            for ingridient in cook_book[dish]:
                new_shop_list_item = dict(ingridient)
                new_shop_list_item['quantity'] *= person_count
                if new_shop_list_item['ingridient_name'] not in shop_list:
                    shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
                else:
                    shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


print(create_dict_from_file('recipes.txt'))

cook_book = create_dict_from_file('recipes.txt')

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, cook_book))