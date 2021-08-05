import os

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
    file_in_dir = {}
    for file_name in list_dir:
        with open(os.path.join(os.getcwd(), dir_name, file_name), encoding='utf-8') as file:
            text_in_file = str()
            for id, line in enumerate(file, 1):
                text_in_file += line
            file_in_dir[file_name] = id, text_in_file
    sorted_file_in_dir = sorted_dict(file_in_dir)
    write_dict_in_file(sorted_file_in_dir, 'sorted_result_file.txt')
    return f'Содержимое файлов в каталоге "{dir_name}" отсортировано и сведено в файл: "sorted_result_file.txt"'

print(find_and_add_file_in_dir('data'))