# Дано вещественное число А и целое число N (>0). Используя один цикл, найти сумму 1+А+А^2 + А^З... + А^Х.
i = 0
ans = 0
try:
    a = float(input('Введите вещественное число')) # проверка является ли ввод вещественным числом
    n = int(input('Введите целое число')) # проверка является ли ввод числом
    while i != n:
        i += 1
        ans += a ** i
    print(ans + 1)  # вывод результата
except ValueError:
    print('Неверный формат') # вывод исключения

