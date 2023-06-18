# 1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Индекс последнего минимального элемента:
# Умножаем все элементы на первый элемент:

import random  # импортируем библиотеку

file = open('file.txt', 'w')  # создаем файл
for i in range(10):
    file.write(f'{random.randrange(-101, 101)}\n')  # наполняем его
file.close()  # закрываем его
file = open('file.txt', 'r')
a = [int(i.replace("\n", "")) for i in file.readlines()]  # считываем данне  файла
file.close()  # закрываем его
new_file = open('new_file.txt', 'w')  # создаем новый файл
print(f' Исходные данные : {a}\n'
      f'Количество элементов : {len(a)}\n'
      f'Индекс последнего минимального элемента : {a.index(min(a))}\n'
      f'Умножаем все элементы на первый элемент: {[i * a[0] for i in a]}', file=new_file)  # наполняем его
new_file.close()  # закрываем его
new_file = open('new_file.txt', 'r')
print(*new_file)  # Выводим результат
