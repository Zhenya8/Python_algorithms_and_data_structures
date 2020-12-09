# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
from random import randint

sequence = [round(randint(-100, 100)) for _ in range(int(input('Сколько элементов будет в списке: ')))]
print(sequence)
new_sequence = []
for i in sequence:
    if i < 0:
        new_sequence.append(i)

min_el = new_sequence[0]
for i in new_sequence:
    if min_el < i:
        min_el = i

print(f'Максимальный отрицательный элемент {min_el}, его индекс'
      f' {new_sequence.index(min_el)}')

# --------------------------------------------------Чуть короче---------------------------------------------------------------

sequence = [round(randint(-100, 100)) for _ in range(int(input('Сколько элементов будет в списке: ')))]
print(sequence)
new_sequence = []
for i in sequence:
    if i < 0:
        new_sequence.append(i)
    min_el = new_sequence[0]
    for j in new_sequence:
        if min_el < j:
            min_el = j

print(f'Максимальный отрицательный элемент {min_el}, его индекс {new_sequence.index(min_el)}')
