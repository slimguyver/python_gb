# https://drive.google.com/file/d/15QTm5svylPBfToNq1wF5mkEg4zjCcggV/view?usp=sharing

n = int(input('Введите целое натурально число: '))
sum_chet = 0
sum_nechet = 0
while n != 0:
    dig = n % 10
    if dig % 2 == 0:
        sum_chet += dig
        n = n // 10
    else:
        sum_nechet += dig
        n = n // 10
print(f'Сумма четных цифр введенного числа = {sum_chet} ')
print(f'Сумма нечетных цифр введенного числа = {sum_nechet}')
