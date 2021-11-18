"""6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет»,
«декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его
содержимое."""

lst = ['сетевое программирование','сокет', 'декоратор']

with open('test_file.txt', 'w', encoding='utf-8') as f_n:
    for f_el in lst:
        f_n.write(f'{f_el}\n')

# # определение кодировки по умолчанию
import locale
default_encoding = locale.getpreferredencoding()
print(default_encoding)

with open('test_file.txt', encoding='utf-8') as f_n:
    for el_str in f_n:
        print(el_str)
    print()
