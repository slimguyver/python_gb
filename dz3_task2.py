import random

size = 20
min_item = 0
max_item = 20
array = [random.randint(min_item, max_item) for i in range(size)]
print(array)

array_result = []
for i in range(len(array) - 1):
    if array[i] % 2 == 0:
        array_result.append(i)

print(f'Позиции четных элементов в массиве: {array_result}')
