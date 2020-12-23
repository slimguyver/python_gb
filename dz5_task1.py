import collections

n = int(input('Введите количество компаний: '))
companies = collections.defaultdict()
good_profit_c = collections.deque()
bad_profit_c = collections.deque()
total_profit = 0
qtr = 4

for i in range(n):
    name = input(f'\nВведите название {i+1}й компании: ')
    profit = 0
    q = 1
    while q <= qtr:
        profit += float(input(f'Введите прибыль за {q}й квартал: '))
        q += 1
    companies[name] = profit
    total_profit += profit

average_profit = total_profit / n

for i, item in companies.items():
    if item >= average_profit:
        good_profit_c.append(i)
    else:
        bad_profit_c.append(i)

print(f'Средняя прибыль для всех компаний составила: {average_profit}')
print(f'Прибыль выше среднего у {len(good_profit_c)} компании(й):')
for name in good_profit_c:
    print(name)
print(f'Прибыль ниже среднего у {len(bad_profit_c)} компании(й):')
for name in bad_profit_c:
    print(name)