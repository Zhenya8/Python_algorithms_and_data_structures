# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque
from collections import Counter

letters = Counter({'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13,
                   'E': 14, 'F': 15})
a = deque(input('Введите первое число: ').upper())
b = deque(input('Введите второе число: ').upper())

print(f'Первое число: {a} \nВторое число: {b}')

# Выравниваем длины введённых чисел
for _ in range(abs(len(a) - len(b))):
    if len(a) > len(b):
        b.appendleft('0')
    if len(b) > len(a):
        a.appendleft('0')

# Разворачиваем для сложения в цикле for in
a.reverse(), b.reverse()

remainder = 0  # остаток от вычитания 16
c = deque([])
for i in range(len(a)):
    c.appendleft((letters.get(a[i]) + letters.get(b[i])) % 16 + remainder)
    remainder = (letters.get(a[i]) + letters.get(b[i])) // 16

res = deque([])
for i in range(len(c)):
    res.append([key for key, values in letters.items() if values == c[i]])
print(f'Результат сложения: ', *res)
