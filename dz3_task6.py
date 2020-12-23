import random

size = 10
min_item = 0
max_item = 32
array = [random.randint(min_item, max_item) for i in range(size)]
i_max = 0
i_min = 0
sum = 0

print(array)

myMax = array[0]
myMin = array[0]

for i in range(size):
    if array[i] > myMax:
        myMax = array[i]
        i_max = i
    if array[i] < myMin:
        myMin = array[i]
        i_min = i

print('Позиция минимального элемента:', i_min, 'Позиция максимального элемента:', i_max)

if i_min < i_max:
    for i in range(i_min + 1, i_max):
        sum += array[i]
elif i_min > i_max:
    for i in range(i_max + 1, i_min):
        sum += array[i]

print(f'Сумма элементов между минимальным и максимальным значениями: {sum}')


