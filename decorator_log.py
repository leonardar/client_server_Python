import sys, os, glob, logging
import inspect
from datetime import datetime


#определение имени файла и установка логера
name = [os.path.basename(x) for x in glob.glob(sys.argv[0])][0][:-3]
LOGGER = logging.getLogger(name)

def log_class_decorator(class_name):
    # class_method = inspect.getmembers(class_name, predicate=inspect.isfunction)[0][0]
    def decorated(func):
        def new_func(self, message):
            res = func(message)
            main_func = inspect.stack()[1][3] # определяем функцию, из которой была вызвана декорированная
            current_datetime = datetime.now()  # определяем дату и время
            LOGGER.debug(f'{current_datetime} Метод {func} класса {class_name} вызван c параметрами {message} из модуля {main_func}')
            return res
        return new_func

    if LOGGER.name == 'client':
        class_name.check_response = decorated(class_name.check_response)
    elif LOGGER.name == 'server':
        class_name.client_message_handler = decorated(class_name.client_message_handler)
    return class_name

def log_func_decorator(func):
    def decorated(*args, **kwargs):
        result = func(*args, **kwargs)
        main_func = inspect.stack()[1][3] # определяем функцию, из которой была вызвана декорированная
        current_datetime = datetime.now() # определяем дату и время
        LOGGER.debug(f'{current_datetime} Функция {func.__name__} вызвана c параметрами {args}, {kwargs} из модуля {main_func}')
        return result
    return decorated
