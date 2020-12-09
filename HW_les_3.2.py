# Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
import random

my_list = [round(random.random() * 100) for i in range(int(input('Сколько элементов будет в списке: ')))]
print(my_list)
index_list = []
for i in my_list:
    if i % 2 == 0:
        index_list.append(my_list.index(i))

print(index_list)

# --------------------------------------------------------------------------------------------------------------------

my_list = [round(random.random() * 100) for i in range(int(input('Сколько элементов будет в списке: ')))]
print(my_list)
index_list = []
for ind, i in enumerate(my_list):
    if i % 2 == 0:
        index_list.append(ind)

print(index_list)
