"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

word_1 = 'разработка'
word_2 = 'администрирование'
word_3 = 'protocol'
word_4 = 'standard'

lst = [word_1,word_2,word_3,word_4]

lst_encode = []
for i in lst:
    i = i.encode('utf-8')
    lst_encode.append(i)
    # print(i, type(i))
print(lst_encode)

lst_decode = []
for i in lst_encode:
    i = i.decode('utf-8')
    lst_decode.append(i)
    # print(i, type(i))
print(lst_decode)
