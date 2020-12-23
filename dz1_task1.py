a = int(input('Введите трехзначное целое число: '))
b = a % 10
a = a // 10
c = a % 10
a = a // 10
digit_sum = a + b + c
digit_com = a * b * c
print(f'Сумма цифр введеного числа равна: {digit_sum} ')
print(f'Произведение цифр введеного числа равна: {digit_com} ')
