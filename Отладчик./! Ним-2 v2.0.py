from random import randint

kychka_one = int(input())
kychka_two = int(input())
one_or_two = 0
while kychka_one != 0 and kychka_two != 0:
    if kychka_one > 1 and kychka_two > 1:
        one_or_two = 2
        randoms = randint(2, kychka_two - 1)
        kychka_two -= randoms
        print(one_or_two, randoms, kychka_one, kychka_two)
    elif kychka_one > 1 and kychka_two < 2:
        one_or_two = 1
        randoms = randint(2, kychka_one - 1)
        kychka_one -= randoms
        print(one_or_two, randoms, kychka_one, kychka_two)
    elif kychka_one < 2 and kychka_two > 1:
        one_or_two = 2
        randoms = randint(2, kychka_two - 1)
        kychka_two -= randoms
        print(one_or_two, randoms, kychka_one, kychka_two)
    elif kychka_one < 2 and kychka_two < 2:
        if kychka_two == 0:
            one_or_two = 1
            print(one_or_two, kychka_two, kychka_one, 0)
            kychka_two = 0
        else:
            one_or_two = 2
            print(one_or_two, kychka_one, 0, kychka_two)
            kychka_one = 0
    if kychka_one == 0 and kychka_two == 0:
        print('ИИ выиграли!')
    # ------------------------------------------------
    players_kychka = int(input())
    players_stone = int(input())
    if players_kychka == 1:
        if kychka_one >= players_stone:
            kychka_one -= players_stone
            print(players_kychka, players_stone, kychka_one, kychka_two)
        else:
            print('Некорректный ход:', players_kychka, players_stone)
            players_kychka = int(input())
            players_stone = int(input())
    elif players_kychka == 2:
        if kychka_two >= players_stone:
            kychka_two -= players_stone
            print(players_kychka, players_stone, kychka_one, kychka_two)
        else:
            print('Некорректный ход:', players_kychka, players_stone)
            players_kychka = int(input())
            players_stone = int(input())
    else:
        print('Некорректный ход:', players_kychka, players_stone)
        players_kychka = int(input())
        players_stone = int(input())
    if kychka_one == 0 and kychka_two == 0:
        print('Вы выиграли!')
