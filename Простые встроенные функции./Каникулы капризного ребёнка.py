city1 = input()
city2 = input()
if ((city1 == 'Тула' and city1 != 'Пенза') or (city2 != 'Тула' and city2 == 'Пенза')) and city2 != city1:
    print('ДА')
else:
    print('НЕТ')
