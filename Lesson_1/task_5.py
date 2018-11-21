# 5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
# преобразовать результаты из байтовового в строковый тип на кириллице.

import subprocess

lst = [
    ['ping', 'yandex.ru'],
    ['ping', 'youtube.com']
]

for args in lst:
    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in subproc_ping.stdout:
        line = line.decode('cp866')
        print(line)
