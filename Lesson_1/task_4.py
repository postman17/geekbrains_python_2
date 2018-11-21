# 4. Преобразовать слова «разработка», «администрирование»,
# «protocol», «standard» из строкового представления в
# байтовое и выполнить обратное преобразование
# (используя методы encode и decode).

lst = [
    'разработка',
    'администрирование',
    'protocol',
    'standard'
]

lst_encode = []
lst_decode = []

for item in lst:
    temp = item.encode('utf-8')
    lst_encode.append(temp)
    lst_decode.append(temp.decode('utf-8'))

print(lst_encode)
print(lst_decode)
