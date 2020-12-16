# Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать,
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.

# В качестве задачи взята 3 задача из урока 3: В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint
import timeit
import cProfile

START = -100
FINISH = 100


# ------------------------------------------------------------- Цикл While -----------------------------------------------------------------

def func_1(x):
    sequence = [round(randint(START, FINISH)) for _ in range(x)]
    min_el = sequence[0]
    max_el = sequence[0]
    print(sequence)

    i = 0
    while len(sequence) > i:
        if min_el > sequence[i]:
            min_el = sequence[i]
        if max_el < sequence[i]:
            max_el = sequence[i]
        i += 1

    min_ind = sequence.index(min_el)
    max_ind = sequence.index(max_el)
    print(f'Минимальное число: {min_el} - sequence[{min_ind}], \nМаксимальное число: {max_el} - sequence[{max_ind}]')
    sequence[min_ind], sequence[max_ind] = sequence[max_ind], sequence[min_ind]
    print(f'Меняем местами минимальный и максимальный элементы: {sequence} END')


# print(timeit.timeit('func_1(10)', number=100, globals=globals()))  # 0.003864900000000001
# print(timeit.timeit('func_1(100)', number=100, globals=globals()))  # от 0.002768699999999999 до 0.011418200000000003
# print(timeit.timeit('func_1(1_000)', number=100, globals=globals()))  # от 0.004533200000000001 до 0.014185499999999997
# print(timeit.timeit('func_1(10_000)', number=100, globals=globals()))  # 0.014277000000000001#

# cProfile.run('func_1(10)')
#          84 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 HW_les_4.1.py:21(func_1)
#         1    0.000    0.000    0.000    0.000 HW_les_4.1.py:22(<listcomp>)
#        10    0.000    0.000    0.000    0.000 random.py:200(randrange)
#        10    0.000    0.000    0.000    0.000 random.py:244(randint)
#        10    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        11    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         3    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#        10    0.000    0.000    0.000    0.000 {built-in method builtins.round}
#        10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        13    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

# cProfile.run('func_1(100)')
#          739 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.000    0.000    0.001    0.001 HW_les_4.1.py:21(func_1)
#         1    0.000    0.000    0.001    0.001 HW_les_4.1.py:22(<listcomp>)
#       100    0.000    0.000    0.000    0.000 random.py:200(randrange)
#       100    0.000    0.000    0.001    0.000 random.py:244(randint)
#       100    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#       101    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         3    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#       100    0.000    0.000    0.000    0.000 {built-in method builtins.round}
#       100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       128    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

# cProfile.run('func_1(1000)')
#          7266 function calls in 0.027 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.027    0.027 <string>:1(<module>)
#         1    0.001    0.001    0.027    0.027 HW_les_4.1.py:21(func_1)
#         1    0.001    0.001    0.009    0.009 HW_les_4.1.py:22(<listcomp>)
#      1000    0.003    0.000    0.006    0.000 random.py:200(randrange)
#      1000    0.001    0.000    0.007    0.000 random.py:244(randint)
#      1000    0.002    0.000    0.003    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.027    0.027 {built-in method builtins.exec}
#      1001    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         3    0.016    0.005    0.016    0.005 {built-in method builtins.print}
#      1000    0.001    0.000    0.001    0.000 {built-in method builtins.round}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1255    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}


# cProfile.run('func_1(10_000)')
#          72779 function calls in 0.091 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.090    0.090 <string>:1(<module>)
#         1    0.011    0.011    0.090    0.090 HW_les_4.1.py:21(func_1)
#         1    0.009    0.009    0.052    0.052 HW_les_4.1.py:22(<listcomp>)
#     10000    0.014    0.000    0.031    0.000 random.py:200(randrange)
#     10000    0.008    0.000    0.039    0.000 random.py:244(randint)
#     10000    0.011    0.000    0.018    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.091    0.091 {built-in method builtins.exec}
#     10001    0.003    0.000    0.003    0.000 {built-in method builtins.len}
#         3    0.025    0.008    0.025    0.008 {built-in method builtins.print}
#     10000    0.004    0.000    0.004    0.000 {built-in method builtins.round}
#     10000    0.003    0.000    0.003    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     12768    0.004    0.000    0.004    0.000 {method 'getrandbits' of '_random.Random' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

# ------------------------------------------------------------- Цикл For in ---------------------------------------------------------------

def func_2(x):
    sequence = [round(randint(START, FINISH)) for _ in range(x)]
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


# print(timeit.timeit('func_2(10)', number=100, globals=globals()))  # 0.011989099999999996
# print(timeit.timeit('func_2(100)', number=100, globals=globals()))  # 0.047984200000000005
# print(timeit.timeit('func_2(1_000)', number=100, globals=globals()))  # 0.4486585
# print(timeit.timeit('func_2(10_000)', number=100, globals=globals()))  # 2.4878641

# cProfile.run('func_2(10)')
#          76 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 HW_les_4.1.py:134(func_2)
#         1    0.000    0.000    0.000    0.000 HW_les_4.1.py:135(<listcomp>)
#        10    0.000    0.000    0.000    0.000 random.py:200(randrange)
#        10    0.000    0.000    0.000    0.000 random.py:244(randint)
#        10    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         3    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#        10    0.000    0.000    0.000    0.000 {built-in method builtins.round}
#        10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        15    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

# cProfile.run('func_2(100)')
#          647 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.000    0.000    0.001    0.001 HW_les_4.1.py:134(func_2)
#         1    0.000    0.000    0.001    0.001 HW_les_4.1.py:135(<listcomp>)
#       100    0.000    0.000    0.000    0.000 random.py:200(randrange)
#       100    0.000    0.000    0.001    0.000 random.py:244(randint)
#       100    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         3    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#       100    0.000    0.000    0.000    0.000 {built-in method builtins.round}
#       100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       136    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

# cProfile.run('func_2(1000)')
#          6262 function calls in 0.019 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.019    0.019 <string>:1(<module>)
#         1    0.000    0.000    0.019    0.019 HW_les_4.1.py:134(func_2)
#         1    0.001    0.001    0.004    0.004 HW_les_4.1.py:135(<listcomp>)
#      1000    0.001    0.000    0.002    0.000 random.py:200(randrange)
#      1000    0.001    0.000    0.003    0.000 random.py:244(randint)
#      1000    0.001    0.000    0.001    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.019    0.019 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         3    0.015    0.005    0.015    0.005 {built-in method builtins.print}
#      1000    0.000    0.000    0.000    0.000 {built-in method builtins.round}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1251    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

# cProfile.run('func_2(10_000)')
#          62691 function calls in 0.048 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.048    0.048 <string>:1(<module>)
#         1    0.007    0.007    0.048    0.048 HW_les_4.1.py:134(func_2)
#         1    0.005    0.005    0.029    0.029 HW_les_4.1.py:135(<listcomp>)
#     10000    0.008    0.000    0.018    0.000 random.py:200(randrange)
#     10000    0.004    0.000    0.022    0.000 random.py:244(randint)
#     10000    0.006    0.000    0.010    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.048    0.048 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         3    0.012    0.004    0.012    0.004 {built-in method builtins.print}
#     10000    0.002    0.000    0.002    0.000 {built-in method builtins.round}
#     10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     12680    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

# ----------------------------- Нахождение мин и макс встроенными инструментами и стандартный обмен ---------------------------------------
# Я не придумала 3его варианта решения  :(

def func_3(x):
    sequence = [round(randint(START, FINISH)) for _ in range(x)]
    print(f'Последовательность - {sequence}')

    min_ind, max_ind = sequence.index(min(sequence)), sequence.index(max(sequence))
    print(f'Минимальное число : {min(sequence)} на позиции : {min_ind} \nМаксимальное число : {max(sequence)} на позиции : {max_ind}')
    sequence[min_ind], sequence[max_ind] = sequence[max_ind], sequence[min_ind]
    print(sequence)

# print(timeit.timeit('func_3(10)', number=100, globals=globals()))  # 0.008569100000000003
# print(timeit.timeit('func_3(100)', number=100, globals=globals()))  # 0.05363280000000001
# print(timeit.timeit('func_3(1_000)', number=100, globals=globals()))  # 0.7981493
# print(timeit.timeit('func_3(10_000)', number=100, globals=globals()))  # 2.4521242

# cProfile.run('func_2(10)')
#          75 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 HW_les_4.1.py:134(func_2)
#         1    0.000    0.000    0.000    0.000 HW_les_4.1.py:135(<listcomp>)
#        10    0.000    0.000    0.000    0.000 random.py:200(randrange)
#        10    0.000    0.000    0.000    0.000 random.py:244(randint)
#        10    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         3    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#        10    0.000    0.000    0.000    0.000 {built-in method builtins.round}
#        10    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        14    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

# cProfile.run('func_2(100)')
#          639 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 HW_les_4.1.py:134(func_2)
#         1    0.000    0.000    0.000    0.000 HW_les_4.1.py:135(<listcomp>)
#       100    0.000    0.000    0.000    0.000 random.py:200(randrange)
#       100    0.000    0.000    0.000    0.000 random.py:244(randint)
#       100    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         3    0.000    0.000    0.000    0.000 {built-in method builtins.print}
#       100    0.000    0.000    0.000    0.000 {built-in method builtins.round}
#       100    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#       128    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

# cProfile.run('func_2(1000)')
#          6275 function calls in 0.008 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.008    0.008 <string>:1(<module>)
#         1    0.000    0.000    0.008    0.008 HW_les_4.1.py:134(func_2)
#         1    0.001    0.001    0.006    0.006 HW_les_4.1.py:135(<listcomp>)
#      1000    0.002    0.000    0.003    0.000 random.py:200(randrange)
#      1000    0.001    0.000    0.004    0.000 random.py:244(randint)
#      1000    0.001    0.000    0.002    0.000 random.py:250(_randbelow_with_getrandbits)
#         1    0.000    0.000    0.008    0.008 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         3    0.002    0.001    0.002    0.001 {built-in method builtins.print}
#      1000    0.000    0.000    0.000    0.000 {built-in method builtins.round}
#      1000    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1264    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
#         2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

# cProfile.run('func_2(10_000)')
#       62749 function calls in 0.042 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.042    0.042 <string>:1(<module>)
#      1    0.003    0.003    0.042    0.042 HW_les_4.1.py:70(func_2)
#      1    0.005    0.005    0.028    0.028 HW_les_4.1.py:71(<listcomp>)
#  10000    0.007    0.000    0.017    0.000 random.py:200(randrange)
#  10000    0.004    0.000    0.021    0.000 random.py:244(randint)
#  10000    0.006    0.000    0.009    0.000 random.py:250(_randbelow_with_getrandbits)
#      1    0.000    0.000    0.042    0.042 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      3    0.011    0.004    0.011    0.004 {built-in method builtins.print}
#  10000    0.002    0.000    0.002    0.000 {built-in method builtins.round}
#  10000    0.001    0.000    0.001    0.000 {method 'bit_length' of 'int' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#  12738    0.002    0.000    0.002    0.000 {method 'getrandbits' of '_random.Random' objects}
#      2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}


# Вывод на основании результата работы функции timeit:
# Судя по полученным цифрам, самым оптимальным подходом является перебор списка из рандомных чисел при помощи цикла while. При увеличении
# входных данных замеры показывают наименьшие затраты времени на обработку.

# Результаты работы функции cProfile показывают, что слабых мест нет ни в одном из алгоритмов. В оптимизации не нуждаются. Во всех время
# растёт линейно.
