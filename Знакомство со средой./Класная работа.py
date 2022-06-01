print('Привет, Яндекс!')
print("Приятно познакомиться.")
shout = 'Ауууу!', 'Ауууууу!'
print(*shout)
print(*shout)


# Планета угадайка
import random
# игра-угадайка с планетами
planets = ['Меркурий', 'Венера', 'Земля', 'Марс',
           'Юпитер', 'Сатурн', 'Уран', 'Нептун']
planet = random.choice(planets)
# !!! выше непонятный код !!!
# к этому моменту в переменной planet лежит правильный ответ
print(planet)
print('Какую планету я загадал?')
answer = input()
# далее программа проверяет, что ответ answer совпал с правильным ответом planet
# !!! ниже непонятный код !!!
if answer == 'Плутон':
    print('Плутон уже не считается планетой.')
elif answer not in planets:
    print('Да это же вообще не название планеты Солнечной системы.')
elif answer == planet:
    print('*** Верно! *** Это', answer)
else:
    print('Неверно!')
# input()


# Попугай
first_str = input()
second_str = input()
third_str = input()
print(first_str)
print(second_str)
print(third_str)


# Билетная касса
print('Билет на', '"', first_str, '"', 'в', '"',second_str, '"','на', '"', third_str, '"', 'забронирован.')