all_stone = int(input())
while all_stone != 0:
    if all_stone % 4 == 1:
        all_stone -= 1
        print(1, all_stone)
    elif all_stone % 4 == 2:
        all_stone -= 2
        print(2, all_stone)
    elif all_stone % 4 == 3:
        all_stone -= 3
        print(3, all_stone)
    else:
        all_stone -= 1
        print(1, all_stone)
    if all_stone == 0:
        print('ИИ выйграл!')

    player = int(input())
    if 0 < player < 4:
        all_stone -= player
        print(player, all_stone)
        if all_stone == 0:
            print('Вы выйграли!')
    else:
        while 3 < player or player < 1:
            print('Некорректный ход:', player)
            player = int(input())
        all_stone -= player
        print(player, all_stone)
