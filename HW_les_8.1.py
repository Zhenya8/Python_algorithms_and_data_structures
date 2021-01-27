# 1) Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка. Требуется вернуть
# количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
# func("papa")
# 6
# func("sova")
# 9
from hashlib import sha256


def sub_string(s):
    sub = set()
    for i in range(len(s)):
        for j in range(len(s) - 1 if i == 0 else len(s), i, -1):
            sub.add(sha256(s[i:j].encode('utf-8')).hexdigest())
    return f'Количество подстрок в строке - "{s}" равно: {len(sub)}\n{sub}'


string = input('Введите строку: ')
print(sub_string(string))

