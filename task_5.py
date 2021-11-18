"""
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на кириллице.
"""
import os
import chardet
import subprocess

URLS = ['yandex.ru','youtube.com']

for url in URLS:
    args = ['ping', '-c 4', url]
    YA_PING = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in YA_PING.stdout:
        result = chardet.detect(line)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))
