# 6. Создать текстовый файл test_file.txt, заполнить
# его тремя строками: «сетевое программирование»,
# «сокет», «декоратор». Проверить кодировку файла по
# умолчанию. Принудительно открыть файл в формате
# Unicode и вывести его содержимое.

# Создание файла 'test_file.txt' с содержимым
with open('test_file.txt', 'w') as file:
    file.write('сетевое программирование\n')
    file.write('сокет\n')
    file.write('декоратор')
print('Файл \'test_file.txt\' создан!')

# Проверка кодировки файла 'test_file.txt'
file = open('test_file.txt', 'r')
file.read()
file.close()
print('Кодировка файла - ', file)

# Принудительное открытие файла 'test_file.txt' и вывод содержимого
with open('test_file.txt', encoding='utf-8') as file:
    for line in file:
        print(line)
# Тут выведется ошибка кодировки при открытии файла