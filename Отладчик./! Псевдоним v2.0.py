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
if 1 < all_stones < 4:
    ii = all_stones - 1
    all_stones -= ii
    print(ii, all_stones)
    print('Вы выйграли!')
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
    ii = all_stones - 1
    all_stones -= ii
    print(all_stones, 1)
elif all_stones == 4:
    II = 3
    all_stones -= II
    print(II, all_stones)
    if 0 < (player := int(input())) < 4 and (player := int(input())) <= all_stones:
        all_stones -= player
        print(player, all_stones)
        print('ИИ выйграл!')
    else:
        print('Некорректный ход:', player)
        player = int(input())
    print('ИИ выйграли!')
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
    print(all_stones - 1, 1)
    if 0 < (player := int(input())) < 4:
        all_stones -= player
        print(player, all_stones)
        print('Вы выиграли!')
    else:
        print('Некорректный ход:', player)
        player = int(input())
elif all_stones == 1:
    print(1,0)
    print('Вы выйграли!')