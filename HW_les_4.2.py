# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.
import math
import timeit
import cProfile


# ------------------------------------------------- Решето Эратосфена ----------------------------------------------------------------------

def prime_1(n):
    up = n * 1000
    sieve = [i for i in range(up)]
    sieve[1] = 0

    for i in range(2, up):
        if sieve[i] != 0:
            j = i * 2  # Аналогично записи i + i. j - доп.переменная, определяющая след.число (2 + 2 = 4 + 2 = 6 и т.п.)
            while j < up:
                sieve[j] = 0
                j += i

    prime_list = [i for i in sieve if i != 0]
    return prime_list[n - 1]


prime_num = int(input('Какое по счёту простое число вывести: '))
print(prime_1(prime_num))


# print(timeit.timeit('prime_1(2)', number=100, globals=globals())) # 0.0899644
# print(timeit.timeit('prime_1(4)', number=100, globals=globals())) # 0.1976169
# print(timeit.timeit('prime_1(8)', number=100, globals=globals())) # 0.4185589
# print(timeit.timeit('prime_1(1000)', number=100, globals=globals())) # 0.8661150000000001


# cProfile.run('prime_1(2)')
#          6 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 HW_les_4.2.py:14(prime_1)
#         1    0.000    0.000    0.000    0.000 HW_les_4.2.py:16(<listcomp>)
#         1    0.000    0.000    0.000    0.000 HW_les_4.2.py:27(<listcomp>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('prime_1(4)')
#          6 function calls in 0.002 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#         1    0.002    0.002    0.002    0.002 HW_les_4.2.py:14(prime_1)
#         1    0.000    0.000    0.000    0.000 HW_les_4.2.py:16(<listcomp>)
#         1    0.000    0.000    0.000    0.000 HW_les_4.2.py:27(<listcomp>)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('prime_1(8)')
#          6 function calls in 0.004 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.004    0.004 <string>:1(<module>)
#         1    0.003    0.003    0.004    0.004 HW_les_4.2.py:14(prime_1)
#         1    0.000    0.000    0.000    0.000 HW_les_4.2.py:16(<listcomp>)
#         1    0.000    0.000    0.000    0.000 HW_les_4.2.py:27(<listcomp>)
#         1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('prime_1(16)')
#          6 function calls in 0.011 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.011    0.011 <string>:1(<module>)
#         1    0.008    0.008    0.010    0.010 HW_les_4.2.py:14(prime_1)
#         1    0.002    0.002    0.002    0.002 HW_les_4.2.py:16(<listcomp>)
#         1    0.000    0.000    0.000    0.000 HW_les_4.2.py:27(<listcomp>)
#         1    0.000    0.000    0.011    0.011 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Данный алгоритм оптимален нахождения небольших чисел, для нахождения 1000ого простого числа timeit выдал 67.91189490000001. Зависимость
# линейная.

# ------------------------------------------------- Не Решето Эратосфена -------------------------------------------------------------------

def prime_2(n):
    prime_list = []
    for i in range(2, 1000):  # ноут старальтельно шумел и пыхтел, но не работал для n * 1000 и даже для 10_000
        if (math.factorial(i - 1) + 1) % i == 0:
            prime_list.append(i)
    return prime_list[n - 1]

# prime_num = int(input('Какое по счёту простое число вывести: '))
# print(prime_2(prime_num))

# print(timeit.timeit('prime_2(2)', number=100, globals=globals())) # 5.0268152
# print(timeit.timeit('prime_2(4)', number=100, globals=globals())) # 5.0115584
# print(timeit.timeit('prime_2(8)', number=100, globals=globals())) # 4.9893674
# print(timeit.timeit('prime_2(16)', number=100, globals=globals())) # 4.995076

# cProfile.run('prime_2(2)')
#          1170 function calls in 0.052 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.052    0.052 <string>:1(<module>)
#         1    0.004    0.004    0.052    0.052 HW_les_4.2.py:34(prime_2)
#         1    0.000    0.000    0.052    0.052 {built-in method builtins.exec}
#       998    0.048    0.000    0.048    0.000 {built-in method math.factorial}
#       168    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('prime_2(4)')
#          1170 function calls in 0.053 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.053    0.053 <string>:1(<module>)
#         1    0.004    0.004    0.053    0.053 HW_les_4.2.py:34(prime_2)
#         1    0.000    0.000    0.053    0.053 {built-in method builtins.exec}
#       998    0.049    0.000    0.049    0.000 {built-in method math.factorial}
#       168    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('prime_2(8)')
#          1170 function calls in 0.052 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.052    0.052 <string>:1(<module>)
#         1    0.004    0.004    0.052    0.052 HW_les_4.2.py:34(prime_2)
#         1    0.000    0.000    0.052    0.052 {built-in method builtins.exec}
#       998    0.048    0.000    0.048    0.000 {built-in method math.factorial}
#       168    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('prime_2(16)')
#          1170 function calls in 0.053 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.053    0.053 <string>:1(<module>)
#         1    0.004    0.004    0.053    0.053 HW_les_4.2.py:34(prime_2)
#         1    0.000    0.000    0.053    0.053 {built-in method builtins.exec}
#       998    0.048    0.000    0.048    0.000 {built-in method math.factorial}
#       168    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Представленный алгоритм очень плох для поиска простого числа. Константная сложность.
