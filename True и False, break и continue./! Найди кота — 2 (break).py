meao = 0
number_of_stroka = 0
while (stroka := input()) != 'СТОП':
    number_of_stroka += 1
    if 'Кот' in stroka or 'кот' in stroka:
        meao = number_of_stroka
        break
print(meao)
