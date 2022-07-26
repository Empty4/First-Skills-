n = int(input())
k = 0
for i in range(n):
    stroki = input()
    if 'Кот' in stroki or 'кот' in stroki:
        print('МЯУ')
        k += 1
        break  # если тут нужно использовать break, то строчки после кота даже ввести не дадут
if k == 0:
    print(-1)
