# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше
# среднего и ниже среднего.

from collections import Counter

n = int(input('Сколько будет фирм: '))
period = 4
firms = Counter({})
for _ in range(n):
    name = (input('Введите название фирмы: '))
    sum_ = 0
    for i in range(period):
        i = int(input('Enter a number: '))
        sum_ += i
    firms[name] = sum_

print(firms)

avg = sum(firms.values()) / len(firms)
print(f'Средняя прибыль для всех предприятий составляет: {avg}')
for key, values in firms.items():
    if values == avg:
        print(f'Предприятие, работает в ноль: "{key}"')
    if values > avg:
        print(f'Предприятие, являющееся прибыльным: "{key}"')
    if values < avg:
        print(f'Предприятие, являющееся убыточным: "{key}"')
