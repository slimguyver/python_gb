import random

size = 20
min_item = 0
max_item = 10
array = [random.randint(min_item, max_item) for i in range(size)]
print(array)

digit = array[0]
m_frequency = 1

for i in range(size - 1):
    frequency = 1
    for k in range(i + 1, size):
        if array[i] == array[k]:
            frequency += 1
    if frequency > m_frequency:
        m_frequency = frequency
        digit = array[i]

if m_frequency > 1:
    print(m_frequency, 'раз(а) встречается число', digit)
else:
    print('В массиве нет одинаковых чисел!')

