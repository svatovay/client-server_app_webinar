import re
import csv

from chardet import detect


def detect_encoding(path):
    with open(path, 'rb') as info_file:
        content = info_file.read()
    return detect(content)['encoding']


def get_data():
    info_files = ('info_1.txt', 'info_2.txt', 'info_3.txt')

    files = {info: detect_encoding(info) for info in info_files}

    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    re_prod = r'Изготовитель системы:\s*([\w|\s]*)\n'
    re_name = r'Название ОС:\s*([\w\s\.]*)\n'
    re_code = r'Код продукта:\s*([\w\-]*)\n'
    re_type = r'Тип системы:\s*([\w\-\s]*)\n'
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    for file, encoding in files.items():
        with open(file, 'r', encoding=encoding) as f_n:
            content = f_n.read()
        os_prod_list.append(re.findall(re_prod, content)[0].strip())
        os_name_list.append(re.findall(re_name, content)[0].strip())
        os_code_list.append(re.findall(re_code, content)[0].strip())
        os_type_list.append(re.findall(re_type, content)[0].strip())
    for i in range(len(main_data[0]) - 1):
        main_data.append([os_prod_list[i], os_name_list[i], os_code_list[i], os_type_list[i]])
    return main_data


def write_to_csv():
    data = get_data()
    with open('main_data.csv', 'w') as f_n:
        f_n_writer = csv.writer(f_n)
        for row in data:
            f_n_writer.writerow(row)


if __name__ == '__main__':
    write_to_csv()
