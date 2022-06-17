import random

# игра-угадайка с планетами
planets = ['Меркурий', 'Венера', 'Земля', 'Марс',
           'Юпитер', 'Сатурн', 'Уран', 'Нептун']
planet = random.choice(planets)
# !!! выше непонятный код !!!
# к этому моменту в переменной planet лежит правильный ответ
warning = 'Присутствует защита от взлома!'
warning = planet
print(warning)
riddle = 'Какую планету я загадал?'
print(riddle)
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
input()
