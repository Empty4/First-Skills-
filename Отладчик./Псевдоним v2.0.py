all_stones = int(input())
II = 3
while all_stones > 6:
    all_stones -= II
    print(II, all_stones)
    if 0 < (player := int(input())) < 4:
        all_stones -= player
        print(player, all_stones)
    else:
        print('Некорректный ход:', player)
        player = int(input())
if all_stones < 4:
    ii = all_stones
    all_stones -= all_stones
    print(ii, all_stones)
    print('ИИ выиграл!')
elif all_stones == 6:
    II = 2
    all_stones -= II
    print(II, all_stones)
    if 0 < (player := int(input())) < 4:
        all_stones -= player
        print(player, all_stones)
    else:
        print('Некорректный ход:', player)
        player = int(input())
    print(all_stones, 0)
elif all_stones == 4:
    II = 1
    all_stones -= II
    print(II, all_stones)
    if 0 < (player := int(input())) < 4:
        all_stones -= player
        print(player, all_stones)
        if all_stones == 3:
            print(all_stones, 0)
            print('Вы выйграли!')
        else:
            print(all_stones, 0)
    else:
        print('Некорректный ход:', player)
        player = int(input())
    print('Вы выйграли!')
elif all_stones == 5:
    II = 1
    all_stones -= II
    print(II, all_stones)
    if 0 < (player := int(input())) < 4:
        all_stones -= player
        print(player, all_stones)
    else:
        print('Некорректный ход:', player)
        player = int(input())
    print(all_stones, 0)
    print('ИИ выиграл!')
