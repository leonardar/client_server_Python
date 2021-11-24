"""
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
 Написать скрипт, автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров — товар (item), количество (quantity),
 цена (price), покупатель (buyer), дата (date). Функция должна предусматривать запись данных в виде словаря в файл
 orders.json. При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""

import json
def write_order_to_json(item,quantity,price,buyer,date):

    DATA = {}
    products = {
        'item':item,
        'quantity':quantity,
        'price':price,
        'buyer':buyer,
        'date':date
    }
    with open('orders.json',encoding='utf-8') as f_n:
        F_N_CONTENT = json.load(f_n)
        DATA.update(F_N_CONTENT)
    for order,list in DATA.items():
        for key,value in products.items():
            list.append({key:value})
    with open('orders.json','w',encoding='utf-8') as f_n:
        json.dump(DATA, f_n, indent=4, ensure_ascii=False)

write_order_to_json('ручка',12,4556,'Иванов','2013-10-21')

