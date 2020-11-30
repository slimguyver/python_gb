# https://drive.google.com/file/d/15QTm5svylPBfToNq1wF5mkEg4zjCcggV/view?usp=sharing

import random

n = random.randint(0, 100)
attemts = 10
i = 0
while attemts >= i:
    m = int(input('Попробуйте угадать число от 0 до 100: '))
    if m != n:
        if m > n:
            print(f'Ваше число {m} больше неизвестного числа!')
            i += 1
        else:
            print(f'Ваше число {m} меньше неизвестного числа!')
            i += 1
    else:
        print('Поздравляю, Вы угадали!')
        break
else:
    print(f'Вы не угадали! Число которое было загадано - {n}')
