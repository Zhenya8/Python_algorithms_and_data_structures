# https://drive.google.com/file/d/1TSD5tUK9Pz5PjbJ6iH4YhDolBMLBw5r8/view?usp=sharing
# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь


n = int(input('Введите целое трёхначное число: '))
a = n // 100
b = n // 10 % 10
c = n % 10
print(f'Сумма цифр числа {n} равна {a + b + c}')
print(f'Произведение цифр {n} равна {a * b * c}')
