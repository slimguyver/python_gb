a, b = 5, 6
bit_or = a | b
bit_and = a & b
bit_xor = a ^ b
print(f'Логические "ИЛИ"= {bit_or} "И"= {bit_and} "XOR"= {bit_xor}')
bit_move_left = a << 2
bit_move_right = a >> 2
print(f'Побитовый сдвиг влево числа 5 на две единицы: {bit_move_left}')
print(f'Побитовый сдвиг вправо числа 5 на две единицы: {bit_move_right}')