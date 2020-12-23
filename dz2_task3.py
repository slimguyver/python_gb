# https://drive.google.com/file/d/15QTm5svylPBfToNq1wF5mkEg4zjCcggV/view?usp=sharing

n = int(input('Введите целое натуральное число, программа развернет его и выдаст результат: '))
print(n)
result = ''
while n != 0:
    dig = str(n % 10)
    result += dig
    n = n // 10
print(result)

