# https://drive.google.com/file/d/15QTm5svylPBfToNq1wF5mkEg4zjCcggV/view?usp=sharing

while True:
     a = int(input('Введите 1ое число: '))
     b = int(input('Введите 2ое число: '))
     zn = input('Введите знак операции (+, -, *, /), введите 0 чтобы закончить работу программы: ')
     if zn == '+':
        plus = a + b
        print(f'Сумма чисел {a} и {b} = {plus}')
     elif zn == '*':
        mul = a * b
        print(f'Произведение чисел {a} и {b} = {mul}')
     elif zn == '-':
        neg = a - b
        print(f'Разность чисел {a} и {b} = {neg}')
     elif zn == '/':
        if b == 0:
            print('Ошибка деления на ноль!')
        else:
            div = a / b
            print(f'Частное чисел {a} и {b} = {div}')
     elif zn == '0':
        break
     else:
        print('Введены некорректные знаки операций!')


