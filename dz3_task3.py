import random

size = 10
min_item = 0
max_item = 32
array = [random.randint(min_item, max_item) for i in range(size)]
i_max = 0
i_min = 0

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

print('Максимальное значение:', myMax, 'Минимальное значение:', myMin)
print('Позиция максимального элемента:', i_max, 'Позиция минимального элемента:', i_min)

array.pop(i_min)
array.pop(i_max)
array.insert(i_min, myMax)
array.insert(i_max, myMin)
print(array)







