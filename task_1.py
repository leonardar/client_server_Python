"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
 info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров «Изготовитель
 системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра
 поместить в соответствующий список. Должно получиться четыре списка — например, os_prod_list,
 os_name_list, os_code_list, os_type_list. В этой же функции создать главный список для хранения
 данных отчета — например, main_data — и поместить в него названия столбцов отчета в виде списка:
 «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов
  также оформить в виде списка и поместить в файл main_data (также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции
реализовать получение данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv().

"""
#!/usr/bin/python3

import csv
from chardet import detect
import re


def get_data():
    main_data = []
    data_names = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []

    for num in range(1,4):
        text_file = f'/Users/leonarda_rain/Downloads/Студентам для решения домашнего задания/info_{num}.txt'
        with open(text_file, 'rb') as f_n:
            CONTENT = f_n.read()
        ENCODING = detect(CONTENT)['encoding']

        with open(text_file, encoding=ENCODING) as f_n:
            CONTENT = f_n.read()
            os_prod = re.search(r'(Изготовитель ОС:)(\s*)(.*)', CONTENT)
            os_prod_list.append(os_prod.groups()[-1])
            os_name = re.search(r'(Название ОС:)(\s*)(.*)', CONTENT)
            os_name_list.append(os_name.groups()[-1])
            os_code = re.search(r'(Код продукта:)(\s*)(.*)', CONTENT)
            os_code_list.append(os_code.groups()[-1])
            os_type = re.search(r'(Тип системы:)(\s*)(.*)', CONTENT)
            os_type_list.append(os_type.groups()[-1])

    main_data.append(data_names)
    for i in range(len(os_prod_list)):
        line = ([os_prod_list[i],os_name_list[i],os_code_list[i],os_type_list[i]])
        print(line)
        main_data.append(line)
    return main_data


def write_to_csv():

    with open('data.csv', 'w', encoding='utf-8') as f_n:
        DATA = get_data()
        F_N_WRITER = csv.writer(f_n)
        F_N_WRITER.writerows(DATA)

write_to_csv()



