all_stone = int(input())
while all_stone != 0:
    if all_stone % 4 == 1:  # Здесь везде ии подставляется когда камней меньше 4 забирая все
        all_stone -= 1
        print(1, all_stone)
    elif all_stone % 4 == 2:
        all_stone -= 2
        print(2, all_stone)
    elif all_stone % 4 == 3:
        all_stone -= 3
        print(3, all_stone)
    else:
        if all_stone % 3 != 0:
            all_stones = all_stone
            all_stone -= all_stone % 3
            print(all_stones % 3, all_stone)
        else:
            all_stones = all_stone
            all_stone -= 3
            print(3, all_stone)
    if all_stone == 0:
        print('Вы выйграли!')

    player = int(input())
    while 3 < player < 1:  # А тут возможен ввод: 4
        print('Некорректный ход:', player)
        player = int(input())
    all_stone -= player
    print(player, all_stone)
    if all_stone == 0:
        print('ИИ выйграл!')
