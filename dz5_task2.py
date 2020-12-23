from collections import defaultdict
from collections import deque


def dex(string):
    '''
    Функция для перевода числа из десятичной
    в шестнадцатиричную систему
    '''
    dex_number = 0
    num = deque(string)
    num.reverse()
    for i in range(len(num)):
        dex_number += table[num[i]] * 16 ** i
    return dex_number


def hex(number):
    '''
    Функция для перевода числа из шестнадцатиричной
    в десятичную систему
    '''
    num = deque()
    while number > 0:
        d = number % 16
        for i in table:
            if table[i] == d:
                num.append(i)
        number //= 16
    num.reverse()
    return list(num)


hex_signs = '0123456789ABCDEF'
table = defaultdict(int)
counter = 0
for key in hex_signs:
    table[key] += counter
    counter += 1

num_1 = dex(input('Введите первое число в шестнадцатиричном формате: ').upper())
num_2 = dex(input('Введите второе число в шестнадцатиричном формате:  ').upper())


print(f'Сумма чисел: {hex(num_1 + num_2)}')
print(f'Произведение чисел: {hex(num_1 * num_2)}')