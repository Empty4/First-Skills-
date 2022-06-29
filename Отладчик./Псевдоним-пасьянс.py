stone = int(input())
while (player := int(input())) != 0:
    if player <= stone and 0 < player < 4:
        stone -= player
    print(stone)
