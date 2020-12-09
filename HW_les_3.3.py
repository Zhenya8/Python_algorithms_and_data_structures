# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import randint

sequence = [round(randint(-100, 100)) for _ in range(int(input('Сколько элементов будет в списке: ')))]
min_el = sequence[0]
max_el = sequence[-1]
print(sequence)

for i in range(len(sequence)):
    if min_el > sequence[i]:
        min_el = sequence[i]
    if max_el < sequence[i]:
        max_el = sequence[i]

min_ind = sequence.index(min_el)
max_ind = sequence.index(max_el)
print(f'Минимальное число: {min_el} - sequence[{min_ind}], \nМаксимальное число: {max_el} - sequence[{max_ind}]')
sequence[min_ind], sequence[max_ind] = sequence[max_ind], sequence[min_ind]
print(f'Меняем местами минимальный и максимальный элементы: {sequence}')
# Не поняла, почему не отрабатывает код ниже, вроде суть та же (строка 18). Не сразу заметила почему-то, видимо, в каких-то
# последовательностях всё
# таки отрабатывает, но при тестировании вроде всё было норм (
# sequence[sequence.index(min_el)], sequence[sequence.index(max_el)] = sequence[sequence.index(max_el)], sequence[sequence.index(min_el)]
