# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). Выведите
# на экран исходный и отсортированный массивы.

from random import uniform

START = 0
STOP = 50


def merge_two(a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]
    return c


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return merge_two(left, right)


array = [round(uniform(START, STOP), 3) for _ in range(int(input('Введите длину списка: ')))]
print(f'Исходный список: {array}')
print(f'Отсортированный список: {merge_sort(array)}')


