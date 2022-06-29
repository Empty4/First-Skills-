day = int(input())
month = int(input())
month -= 2
year = int(input())
vek = year // 100
year = year % 100
answer = day + ((13 * month - 1) // 5) + year + (year // 4 + vek // 4 - 2 * vek + 777)
print(answer % 7)
