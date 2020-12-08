import random

size = 10
min_item = 0
max_item = 20
array = [random.randint(min_item, max_item) for i in range(size)]
i_min_1 = 0
i_min_2 = 0

print(array)

myMin_1 = array[0]
myMin_2 = array[0]

for i in range(size):
    if array[i] < myMin_1:
        myMin_1 = array[i]
        i_min_1 = i

array.pop(i_min_1)

for i in range(len(array)):
    if array[i] < myMin_2:
        myMin_2 = array[i]
        i_min_2 = i

print(f'Первое наименьшее число = {myMin_1}. Второе наименьшее число = {myMin_2}.')
