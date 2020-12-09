# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, надо вывести 6843.


BASE = 10


def reverse_num(n):
    if n < BASE:
        return n
    return int(str(n % 10) + str(reverse_num(n // BASE)))


n = int(input('Введите число: '))
print(reverse_num(n))
