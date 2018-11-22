# 1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов
# info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:
# Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными,
# их открытие и считывание данных. В этой функции из считанных данных необходимо с помощью
# регулярных выражений извлечь значения параметров «Изготовитель системы», «Название ОС»,
# «Код продукта», «Тип системы». Значения каждого параметра поместить в соответствующий список.
# Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list, os_type_list.
# В этой же функции создать главный список для хранения данных отчета — например, main_data —
# и поместить в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС»,
# «Код продукта», «Тип системы». Значения для этих столбцов также оформить в виде списка и поместить
# в файл main_data (также для каждого файла);
# Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать
# получение данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
# Проверить работу программы через вызов функции write_to_csv().

import re
import csv


def get_data(lst):
    os_prod_list, os_name_list, os_code_list, os_type_list = [], [], [], []
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    for file_name in lst:
        with open(file_name) as file:
            data = file.read()
            os_prod = re.search(r'Изготовитель системы\W+\w+', data)
            os_prod_temp = os_prod.group(0).split()
            os_prod_list.append(os_prod_temp[len(os_prod_temp)-1])
            os_name = re.search(r'Название ОС\W+.+', data)
            os_name_temp = os_name.group(0).split(':')
            os_name_list.append(os_name_temp[len(os_name_temp)-1].lstrip())
            os_code = re.search(r'Код продукта\W+.+', data)
            os_code_temp = os_code.group(0).split(':')
            os_code_list.append(os_code_temp[len(os_code_temp) - 1].lstrip())
            os_type = re.search(r'Тип системы\W+.+', data)
            os_type_temp = os_type.group(0).split(':')
            os_type_list.append(os_type_temp[len(os_type_temp) - 1].lstrip())
    for num in range(0, len(main_data[0])-1):
        temp_list = []
        temp_list.append(os_prod_list[num])
        temp_list.append(os_name_list[num])
        temp_list.append(os_code_list[num])
        temp_list.append(os_type_list[num])
        main_data.append(temp_list)
    return main_data


def write_to_csv(filname):
    list_files = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    data = get_data(list_files)
    with open(filname, 'w') as file:
        file_writer = csv.writer(file)
        for row in data:
            file_writer.writerow(row)

write_to_csv('temp.csv')
# Сделал задание как понял условие. Считаю условия задачи слишком запутанными и не эффективными.)))