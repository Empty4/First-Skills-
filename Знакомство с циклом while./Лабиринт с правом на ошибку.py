print('СТРАЖНИК: Привет, путник! Ты смог дойти до храма вечности, это действительно поражает! Теперь тебе надо выбрать вход. \
Я желаю тебе удачи! И не помри там!')
print('')
print('    / \    ', '    / \    ', '    / \    ')
print('   /   \   ', '   /   \   ', '   /   \   ')
print('  /     \  ', '  /     \  ', '  /     \  ')
print('  |     |  ', '  |     |  ', '  |     |  ')
print('  |  1  |  ', '  |  2  |  ', '  |  3  |  ')
print('  |     |  ', '  |     |  ', '  |     |  ')
print('  |     |  ', '  |     |  ', '  |     |  ')
print('  [_____]  ', '  [_____]  ', '  [_____]  ')
choice = input()
if choice == '1':
    print('Первая дверь открылась и ты предстал перед пятиглавой змеёй в 6 футов ростом.')
    print('Какую голову отрубишь первой?')
    choice2 = input()
    if choice2 == '1':
        print('Тебя съели, ты не успел ничего сделать(')
    elif choice2 == '2':
        print('Тебя съели, ты не успел ничего сделать(')
    elif choice2 == '3':
        print('Тебя съели, ты не успел ничего сделать(')
    elif choice2 == '4':
        print('Отрубив эту голову, ты поочереди отрубил и остальный.')
        print('*Ты победил босса храма*')
        print('В награду:')
        print('СЛАВА +10')
        print('ЗОЛОТО +15')
    elif choice2 == '5':
        print('Тебя съели, ты не успел ничего сделать(')
    else:
        print('Голов не так уж много, чтобы ты не смог их посчитать!')
elif choice == '2':
    print('Ты зашёл во вторую дверь и пошёл вперёд, пытаясь различить что-либо в кромешной темноте.')
    print('Ты сделал шаг вперёд и упал в яму с ядовитыми шипами.')
    print('Ты мёртв(')
elif choice == '3':
    print('Ты приложил все усилия, но так и не смог открыть эту дверь.')
    print('СТРАЖНИК: Путник, неужели ты настолько слаб?! Иди от сюда по добру по здорову!')
else:
    choice = input()#я могу запихнуть это в def, но это ещё не пройдено