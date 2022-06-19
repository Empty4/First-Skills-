k = 0
max = 0
min = 190
while (hight := input()) != '!':
    hight = int(hight)
    if 150 < hight < 190:
        k += 1
        if min > hight:
            min = hight
        if max < hight:
            max = hight
print(k)
print(min, max)
