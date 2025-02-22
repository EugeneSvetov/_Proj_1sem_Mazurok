# Вариант 15.
# 1.В последовательности на n целых чисел найти и вывести:
# 1. максимальный среди положительных
# 2. минимальный среди отрицательных
# 3. произведение элементов

import random
import math

lst = [random.randint(-50, 50) for _ in range(int(input('Введите количество чисел : ')))]
print(f'Ваша последовательность : {sorted(lst)}\n'
      f'Максимальное число среди положительных : {max([item for item in lst if item >= 0])}\n'
      f'Минимальное число среди отрицательных : {min([item for item in lst if item <= 0])}\n'
      f'Произведение всех элементов: {math.prod(lst)}')
