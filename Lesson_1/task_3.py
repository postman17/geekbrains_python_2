# 3. Определить, какие из слов «attribute», «класс», «функция»,
# «type» невозможно записать в байтовом типе.


lst = ['attribute', 'класс', 'функция', 'type']

for item in lst:
    try:
        bytes(item, encoding='ASCII')
    except UnicodeEncodeError:
        print(f'Слово \'{item}\' невозможно преобразовать.')



