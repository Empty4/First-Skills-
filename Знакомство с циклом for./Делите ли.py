number = int(input())
k = 0
for i in range(1, number + 1):
    if number % i == 0:
        print(i, end=' ')
        k += 1
if k == 2:
    print('\nПРОСТОЕ')
else:
    print('\nНЕТ')
