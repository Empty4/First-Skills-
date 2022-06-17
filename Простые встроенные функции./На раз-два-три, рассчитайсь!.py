boris = int(input())
vova = int(input())
dima = int(input())
spisok = []
spisok.append(boris)
spisok.append(vova)
spisok.append(dima)
spisok.sort(reverse=True)
for i in spisok:
    print(i)
