# 2. Каждое из слов «class», «function», «method» записать в байтовом
# типе без преобразования в последовательность кодов
# (не используя методы encode и decode) и определить тип,
# содержимое и длину соответствующих переменных.

a, b, c = b'class', b'function', b'method'

print(type(a), type(b), type(c))
print(a, b, c)
print(len(a), len(b), len(c))
