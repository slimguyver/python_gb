x1 = int(input('Введите координату "x" первой точки: '))
y1 = int(input('Введите координату "y" первой точки: '))
x2 = int(input('Введите координату "x" второй точки: '))
y2 = int(input('Введите координату "y" второй точки: '))
if x1 - x2 != 0:
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    print(f'Итоговое уравнение прямой согласно введенных координат:  y = {k}x + {b}')
else:
    print('Error')
