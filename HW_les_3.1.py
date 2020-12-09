# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

sequence = []
for i in range(2, 10):
    count = 0
    for j in range(2, 100):
        if j % i == 0:
            count += 1
    i += 1
    sequence.append(count)

for ind, i in enumerate(sequence):
    print(f'Для числа: {ind + 2} кратных от 2 до 99 оказалось: {i}')
