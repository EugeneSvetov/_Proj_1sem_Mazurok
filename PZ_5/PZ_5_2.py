# Дан прямоугольник, длины сторон которого равны натуральным числам А и В.
# Составить функцию, которая будет находить на сколько квадратов можно разрезать
# данный прямоугольник, если от него каждый раз отрезать квадрат наибольшей
# площади.
def squares(a, b): # объявление функции и ее аргументов
    return (1 if a == b else
            1 + squares((a - b), b) if a > b else
            1 + squares(a, b - a))

try:
    print(squares(int(input('Введите первую сторону прямоугольника ')), int(input('Введите Вторую сторону прямоугольника ')))) # вызов функции
except ValueError:
    print('Неверный формат ввода')