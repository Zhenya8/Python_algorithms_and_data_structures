# # В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.
from random import randint

sequence = [randint(-100, 100) for _ in range(int(input('Сколько элементов будет в списке: ')))]

min_el = sequence[0]
max_el = sequence[-1]
print(sequence)
for i in sequence:
    if min_el > i:
        min_el = i
    if max_el < i:
        max_el = i

min_ind = sequence.index(min_el)
max_ind = sequence.index(max_el)
print(f'Минимальное число: {min_el} - sequence[{min_ind}], \nМаксимальное число: {max_el} - sequence[{max_ind}]')

if min_ind > max_ind:
    sequence = sequence[min_ind:max_ind:-1]
print(sequence)

summ = 0
for i in sequence[1:]:
    summ += i

print(summ)

