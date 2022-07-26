summ = 0
count = 0
while (number := int(input())) != 0:
    summ += number
    count += 1
    if summ == 10:
        print(count)
        break
