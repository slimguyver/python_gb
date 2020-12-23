# https://drive.google.com/file/d/15QTm5svylPBfToNq1wF5mkEg4zjCcggV/view?usp=sharing

def left_side_eq(n):
    if n == 1:
        return n
    elif n > 0:
        return n + left_side_eq(n-1)

def right_side_eq(n):
    return n * (n + 1) // 2

while True:
    n = 7
    if left_side_eq(n) == right_side_eq(n):
        print(f'Для n={n} - Левые и правая части уравнения равны.')
        break
    else:
        print(f'Для n={n} - Левые и правая части уравнения не равны')
        break




