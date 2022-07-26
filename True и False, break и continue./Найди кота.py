n = int(input())
meao = False
for i in range(n):
    stroki = input()
    if 'Кот' in stroki or 'кот' in stroki:
        meao = True
if meao:
    print('МЯУ')
else:
    print('НЕТ')
